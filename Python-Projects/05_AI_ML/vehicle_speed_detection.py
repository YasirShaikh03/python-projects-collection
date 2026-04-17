import cv2
import numpy as np
from ultralytics import YOLO
import time

# Load YOLO model (pretrained on COCO dataset)
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt for better accuracy

# Video path
video_path = r"A:\for small phython project\zcode\WhatsApp Video 2025-10-19 at 21.41.21_04baa7ff.mp4"
cap = cv2.VideoCapture(video_path)

# Pixels to real world conversion (example: 1 pixel = 0.05 meters, you can adjust)
pixel_to_meter = 0.05  

# Store previous positions of detected objects
object_positions = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # YOLO detection
    results = model(frame)[0]  # get detections for current frame

    for r in results.boxes:
        x1, y1, x2, y2 = map(int, r.xyxy[0])  # bounding box
        conf = r.conf[0]
        cls = int(r.cls[0])

        # Only consider vehicles (COCO classes 2, 3, 5, 7: car, motorcycle, bus, truck)
        if cls in [2,3,5,7]:
            cx = int((x1 + x2)/2)
            cy = int((y1 + y2)/2)

            object_id = f"{cls}_{x1}_{y1}"  # temporary object ID

            if object_id in object_positions:
                prev_cx, prev_cy, prev_time = object_positions[object_id]
                dx = cx - prev_cx
                dy = cy - prev_cy
                dist = np.sqrt(dx**2 + dy**2) * pixel_to_meter  # distance in meters
                dt = time.time() - prev_time
                if dt > 0:
                    speed = dist / dt  # meters per second
                    cv2.putText(frame, f"{speed:.2f} m/s", (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
            # Update position
            object_positions[object_id] = (cx, cy, time.time())

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("Detection + Speed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
