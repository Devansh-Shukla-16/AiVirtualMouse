# 🖱️ AI Virtual Mouse using Python, OpenCV & MediaPipe

This project allows you to control your mouse cursor using hand gestures detected via webcam — no physical mouse required! Built using Python, OpenCV, MediaPipe, and AutoPy.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe
- Cursor control based on hand movement
- Gesture-based clicking (e.g., index + middle finger together)
- No external hardware required
- Works with most webcams

---

## 🛠️ Technologies Used

- **Python 3.9**
- **OpenCV** – for video frame processing
- **MediaPipe** – for hand landmark detection
- **AutoPy** – for controlling mouse movement and clicks
- **NumPy** – for coordinate calculations

---

---

## 🔧 Setup Instructions

### Step 1: Create & Activate Virtual Environment (Python 3.9)
  python -m venv .venv
  .venv\Scripts\activate  # Windows


Step 2: Install Dependencies
  pip install opencv-python mediapipe autopy numpy==1.23.5

Step 3: Run the python program
  python main.py


| Gesture                     | Action             |
| --------------------------- | ------------------ |
| Move Hand                   | Moves Mouse Cursor |
| Index + Middle Finger Close | Mouse Click        |


