import cv2
import numpy as np
import math

# ---------- CONFIGURABLE PARAMETERS ----------

# Skin color range in HSV (you may have to tune these for your lighting / skin tone)
LOWER_SKIN = np.array([0, 30, 60], dtype=np.uint8)
UPPER_SKIN = np.array([20, 150, 255], dtype=np.uint8)

# Distance thresholds (in pixels) for state transitions
DANGER_THRESH = 60      # <= this distance -> DANGER
WARNING_THRESH = 160    # <= this distance -> WARNING, else SAFE

# Morphological operation parameters
KERNEL = np.ones((5, 5), np.uint8)


def compute_point_to_rect_distance(px, py, x1, y1, x2, y2):
    """
    Compute shortest Euclidean distance from point (px, py)
    to axis-aligned rectangle with corners (x1, y1) - (x2, y2).
    If point is inside the rectangle, distance = 0.
    """
    # Distance in x-direction
    if px < x1:
        dx = x1 - px
    elif px > x2:
        dx = px - x2
    else:
        dx = 0

    # Distance in y-direction
    if py < y1:
        dy = y1 - py
    elif py > y2:
        dy = py - y2
    else:
        dy = 0

    return math.sqrt(dx * dx + dy * dy)


def classify_state(distance):
    """
    Return SAFE / WARNING / DANGER based on distance to virtual object.
    """
    if distance <= DANGER_THRESH:
        return "DANGER"
    elif distance <= WARNING_THRESH:
        return "WARNING"
    else:
        return "SAFE"


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # We will compute virtual box once we know the frame size
    virtual_box_defined = False
    x1 = y1 = x2 = y2 = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip horizontally for a mirror-like effect
        frame = cv2.flip(frame, 1)

        h, w = frame.shape[:2]

        # Define the virtual object (a box) in the center of the frame
        if not virtual_box_defined:
            box_size = min(w, h) // 4  # size relative to frame
            cx, cy = w // 2, h // 2
            x1, y1 = cx - box_size, cy - box_size
            x2, y2 = cx + box_size, cy + box_size
            virtual_box_defined = True

        # ----------- HAND SEGMENTATION (SKIN COLOR) -----------

        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold for skin color
        mask = cv2.inRange(hsv, LOWER_SKIN, UPPER_SKIN)

        # Clean up mask
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, KERNEL, iterations=2)

        # Find contours on the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        hand_center = None
        state = "SAFE"
        distance = None

        if contours:
            # Choose the largest contour (most likely the hand)
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            # Reject small noisy blobs
            if area > 3000:
                # Draw contour
                cv2.drawContours(frame, [largest_contour], -1, (255, 0, 0), 2)

                # Compute centroid of the contour using moments
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    hand_center = (cX, cY)
                    cv2.circle(frame, hand_center, 7, (255, 0, 255), -1)
                    cv2.putText(frame, "Hand", (cX - 20, cY - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

                    # Compute distance from hand center to virtual box
                    distance = compute_point_to_rect_distance(cX, cY, x1, y1, x2, y2)

                    # Classify state
                    state = classify_state(distance)

        # ----------- VISUAL OVERLAY -----------

        # Color of box based on state
        if state == "SAFE":
            box_color = (0, 255, 0)      # green
        elif state == "WARNING":
            box_color = (0, 255, 255)    # yellow
        else:
            box_color = (0, 0, 255)      # red

        # Draw virtual box
        cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 3)

        # Draw state text
        text = f"STATE: {state}"
        cv2.putText(frame, text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, box_color, 2)

        # Distance text (debug)
        if distance is not None:
            cv2.putText(frame, f"Distance: {int(distance)} px", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # DANGER overlay
        if state == "DANGER":
            cv2.putText(frame, "DANGER DANGER", (w // 8, h // 2),
                        cv2.FONT_HERSHEY_DUPLEX, 2.0, (0, 0, 255), 4)

        # Show the windows
        cv2.imshow("Hand Tracking - POC", frame)
        cv2.imshow("Mask (debug)", mask)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):  # ESC or q to quit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
