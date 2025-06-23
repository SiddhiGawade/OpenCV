# OpenCV & Robotics Projects Repository

This repository contains a collection of OpenCV-based image/video processing programs, a Hearing Aid enhancement project using a pre-trained model, and a YOLOv8-based object detection system for a Robotics project.

---

### 📁 Directory Structure

<pre>

OPEN-CV/
├── .venv/                        # Python virtual environment
├── cloning/
├── data/
├── HearingAid/                   # Hearing Aid project using a pre-trained model
├── Project/
├── Robotics \ yolovenv/          # Robotics project using YOLOv8
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   ├── car1.jpg
│   ├── object_detection.py
│   ├── object_detection_video.py
│   ├── output.mp4
│   ├── pyvenv.cfg
│   └── yolov8n.pt                # Pre-trained YOLOv8 Nano model
│
└── Testing/                      # OpenCV practice programs
    ├── 1_images.py
    ├── 2_video.py
    ├── 3_shapes.py
    ├── 4_mouseEvents1.py
    ├── 5_mouseEvents2.py
    ├── 6_mouseEvents3.py
    ├── 7_cvOperations.py
    ├── 8_ROI.py
    ├── 9_add2Images.py
    ├── 10_bitwiseOperations.py
    ├── 11_trackbar.py
    ├── 12_trackbar2.py
    ├── 13_hsv.py
    ├── 14_simple_thresholding.py
    ├── 15_adaptive_thresholding.py
    ├── 16_otsu_thresholding.py
    ├── 17_matplotlib.py
    ├── 18_simple_thresholding_in_matplotlib.py
    ├── 19_morphological_transformations.py
    ├── 20_smoothing_images.py
    ├── 21_image_gradients.py
    ├── 22_pyramids.py
    ├── 23_motion_detection.py
    ├── 24_face_detection.py
    ├── 25_eye_detection.py
    ├── 26_record_video.py
    ├── balls.jpg
    ├── car1.jpg
    ├── car2.jpeg
    ├── cd_pic.jpeg
    ├── chrome.jpg
    └── gradient.jpeg

</pre>

---

✅ Copy and paste the entire block above into your `README.md`. It will now render cleanly in GitHub with proper indentation and visual hierarchy. Let me know if you'd like to include icons or links as well!

---

## 🔬 OpenCV Programs – `Testing/`

The `Testing` folder includes over 25 Python programs built using **OpenCV**, which demonstrate:

- 🖼️ Image & video display: `1_images.py`, `2_video.py`
- 🖌️ Shape drawing & mouse events: `3_shapes.py` to `6_mouseEvents3.py`
- 🧪 Image operations: `7_cvOperations.py` to `10_bitwiseOperations.py`
- 🎚️ Trackbars & thresholding: `11_trackbar.py` to `16_otsu_thresholding.py`
- 📈 Visualization: `17_matplotlib.py`, `18_simple_thresholding_in_matplotlib.py`
- 🔍 Transformations & smoothing: `19` to `22`
- 🕵️ Motion & face/eye detection: `23_motion_detection.py` to `25_eye_detection.py`
- 📹 Video capture: `26_record_video.py`

---

## 🦻 Hearing Aid Project

A deep learning-based approach to **speech enhancement** designed to help hearing-impaired users.

- Used a **pre-trained audio enhancement model**
- Applied techniques like denoising and clarity improvement
- Built using `TensorFlow`, `librosa`, and `soundfile`

---

## 🤖 Robotics Object Detection (YOLOv8)

A project under `Robotics \ yolovenv/` using **YOLOv8 Nano** for object detection:

- `object_detection.py`: Detection from images
- `object_detection_video.py`: Real-time webcam/video detection
- `yolov8n.pt`: Pre-trained YOLOv8 nano model from [Ultralytics](https://github.com/ultralytics/ultralytics)

📦 Output: Annotated video saved as `output.mp4`

---

## ⚙️ Getting Started

### 🔧 Setup Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

cd Testing
python 1_images.py
