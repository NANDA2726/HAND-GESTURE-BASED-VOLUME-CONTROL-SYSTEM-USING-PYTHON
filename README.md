Overview
This project is a real-time hand gesture-based volume control system that allows users to control system volume using finger movements. It uses computer vision to detect hand landmarks and adjusts volume based on the distance between the thumb and index finger.

Features
  * Real-time hand tracking using webcam
  * Gesture-based volume control
  * Visual feedback with volume bar and percentage
  * Touchless and user-friendly interaction
 

Technologies Used
  * Python
  * OpenCV
  * MediaPipe
  * OS

Installation
1. Clone the repository
git clone https://github.com/NANDA2726/hand-gesture-volume-control.git
cd hand-gesture-volume-control
2. Install dependencies
3.Run the program: python handtracking.py

How It Works
1.Webcam captures live video
2.Hand is detected using MediaPipe
3.Landmarks of thumb and index finger are identified
4.Distance between fingers is calculated
5.Distance is mapped to system volume
6.Volume is adjusted in real time

Output
1.Live webcam feed
2.Hand tracking visualization
3.Volume bar
4.Volume percentage

Requirements
1.Webcam
2.Windows OS (for volume control using Pycaw)
3.Proper lighting

Future Improvements
  * Add gesture controls for play/pause
  * Implement smooth volume control
  * Support multiple gestures
  * Cross-platform support (Windows/Linux)

Author:
  Nanda K

Acknowledgment:
  This project is inspired by advancements in computer vision and gesture-based interaction systems.

License:
  This project is for educational purposes.
