<html>
  <body>
<h1>Hand Danger Detection Prototype</h1>

<h2>Objective</h2>
<p>The prototype tracks a user’s hand in real time using a webcam and detects when the hand approaches a virtual boundary on the screen. When the hand is too close, a warning message “DANGER DANGER” is displayed.
The project demonstrates: - Real-time hand tracking without MediaPipe / OpenPose / cloud APIs - Classical computer vision techniques - A virtual object boundary on the camera feed - Distance-based state classification: SAFE / WARNING / DANGER - Visual on‑screen feedback - Performance > 8 FPS (CPU‑only).</p>
<p>
  <b>Processing Pipeline</b>
<li>
<ol>Capture frame from webcam.</ol>
<ol>Flip horizontally for natural mirror‑style control.</ol>
<ol>Convert to HSV color space.</ol>
<ol>Threshold skin color region using skin range mask.</ol>
<ol>Clean mask using morphological operations.</ol>
<ol>Find contours → select largest contour as hand.</ol>
<ol>Compute centroid of the contour (representing hand position).</ol>
<ol>Calculate distance from hand to virtual object boundary.</ol>
<ol>Determine state based on thresholds.</ol>
<ol>Render overlays and warnings.</ol>
</li>
</p>
<p>
  <h4>System Requirements</h4>
<b>Software</b><br>
•	Python 3.8+<br>
•	OpenCV<br>
•	NumPy<br>
<b></b>Installation</b><br>
pip install opencv-python numpy<br>
<b></b>Run the Application</b><br>
python hand_danger_poc.py<br>
<b></b>Controls</b><br>
<b>Action	Key</b><br>
Quit program	q or ESC<br>
Force stop (terminal)	Ctrl + C<br>
</p>
</body>
</html>
