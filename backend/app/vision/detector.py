# 

import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

CONFIDENCE_THRESHOLD = 0.5

def detect_objects(image_bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = model(img)
    detections = []

    for r in results:
        for box in r.boxes:
            confidence = float(box.conf[0])
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            detections.append({
                "label": label,
                "confidence": round(confidence, 2)
            })

    return detections

