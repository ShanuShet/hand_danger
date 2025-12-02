<html>
  <body>
<h1>Hand Danger Detection Prototype</h1>

<h2>Objective</h2>
<p>The prototype tracks a user’s hand in real time using a webcam and detects when the hand approaches a virtual boundary on the screen. When the hand is too close, a warning message “DANGER DANGER” is displayed.
The project demonstrates: - Real-time hand tracking without MediaPipe / OpenPose / cloud APIs - Classical computer vision techniques - A virtual object boundary on the camera feed - Distance-based state classification: SAFE / WARNING / DANGER - Visual on‑screen feedback - Performance > 8 FPS (CPU‑only).</p>
<p>
  <b>Processing Pipeline</b>
1.	Capture frame from webcam
2.	Flip horizontally for natural mirror‑style control
3.	Convert to HSV color space
4.	Threshold skin color region using skin range mask
5.	Clean mask using morphological operations
6.	Find contours → select largest contour as hand
7.	Compute centroid of the contour (representing hand position)
8.	Calculate distance from hand to virtual object boundary
9.	Determine state based on thresholds
10.	Render overlays and warnings

</p>
<p>
  <h4>System Requirements</h4>
<b>Software</b>
•	Python 3.8+
•	OpenCV
•	NumPy
<b></b>Installation</b>
pip install opencv-python numpy
<b></b>Run the Application</b>
python hand_danger_poc.py
<b></b>Controls</b>
Action	Key
Quit program	q or ESC
Force stop (terminal)	Ctrl + C
</p>
</body>
</html>
