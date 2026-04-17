# 🤖 05 — AI / ML Projects

Computer Vision and Machine Learning applications.

## Scripts

| File | Description |
|------|-------------|
| `face_detection.py` | Real-time face detection using OpenCV Haar Cascade via webcam |
| `vehicle_speed_detection.py` | Estimates vehicle speed from video using YOLOv8 |
| `smart_health_ai.py` | Health AI — food calories, BMR calculator, posture detection (MediaPipe) |
| `smart_academic_system.py` | Student dashboard — marks input, ML pass/fail prediction, PDF report |

## Run

```bash
pip install opencv-python mediapipe ultralytics numpy scikit-learn matplotlib fpdf Pillow
```

```bash
python face_detection.py
python vehicle_speed_detection.py
```

## Setup Notes

### `vehicle_speed_detection.py`
- Update `video_path` to point to your local video file.
- `yolov8n.pt` downloads automatically on first run.

### `smart_health_ai.py`
- Requires a working webcam for posture detection.
- Food database is hardcoded — expand `FOOD_CALORIES` dict as needed.

### `smart_academic_system.py`
- Requires companion modules: `db.py`, `ml_model.py`, `analyzer.py`, `report.py`, `dashboard.py`.
- This is the main entry point of a larger project.
