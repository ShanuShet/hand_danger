Hand Danger Detection Prototype Documentation

Objective
The prototype tracks a user’s hand in real time using a webcam and detects when the hand approaches a virtual boundary on the screen. When the hand is too close, a warning message “DANGER DANGER” is displayed.
The project demonstrates: - Real-time hand tracking without MediaPipe / OpenPose / cloud APIs - Classical computer vision techniques - A virtual object boundary on the camera feed - Distance-based state classification: SAFE / WARNING / DANGER - Visual on‑screen feedback - Performance > 8 FPS (CPU‑only)
