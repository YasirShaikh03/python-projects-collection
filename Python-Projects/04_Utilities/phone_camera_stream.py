import cv2
import numpy as np

# IP Webcam video URL
url = "http://192.168.0.105:8080/video"


# Capture video
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()  # use same variable 'cap'
    if ret and frame is not None:
        cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
