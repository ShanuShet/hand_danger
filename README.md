<html>
  <body>
<h1>Hand Danger Detection Prototype</h1>

<h2>Objective</h2>
<p>The prototype tracks a user’s hand in real time using a webcam and detects when the hand approaches a virtual boundary on the screen. When the hand is too close, a warning message “DANGER DANGER” is displayed.</p>
<p>The project demonstrates: - Real-time hand tracking without MediaPipe / OpenPose / cloud APIs - Classical computer vision techniques - A virtual object boundary on the camera feed - Distance-based state classification: SAFE / WARNING / DANGER - Visual on‑screen feedback - Performance > 8 FPS (CPU‑only).</p>
<p>
  <b>Processing Pipeline</b>
<ol>
<li>Capture frame from webcam.</li>
<li>Flip horizontally for natural mirror‑style control.</li>
<li>Convert to HSV color space.</li>
<li>Threshold skin color region using skin range mask.</>li
<li>Clean mask using morphological operations.</li>
<li>Find contours → select largest contour as hand.</li>
<li>Compute centroid of the contour (representing hand position).</li>
<li>Calculate distance from hand to virtual object boundary.</li>
<li>Determine state based on thresholds.</li>
<li>Render overlays and warnings.</li>
</ol>
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
