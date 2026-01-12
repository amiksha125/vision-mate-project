

# import cv2
# import numpy as np
# from ultralytics import YOLO

# model = YOLO("yolov8n.pt")

# CONFIDENCE_THRESHOLD = 0.5

# IMPORTANT_OBJECTS = {
#     "person", "chair", "door", "table",
#     "car", "bicycle", "bus", "stairs"
# }

# def get_position(x_center, img_width):
#     if x_center < img_width / 3:
#         return "left"
#     elif x_center < 2 * img_width / 3:
#         return "front"
#     else:
#         return "right"

# def detect_objects(image_bytes):
#     np_img = np.frombuffer(image_bytes, np.uint8)
#     img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

#     img_height, img_width, _ = img.shape
#     results = model(img)

#     detections = []

#     for r in results:
#         for box in r.boxes:
#             confidence = float(box.conf[0])
#             if confidence < CONFIDENCE_THRESHOLD:
#                 continue

#             cls_id = int(box.cls[0])
#             label = model.names[cls_id]

#             if label not in IMPORTANT_OBJECTS:
#                 continue

#             x1, y1, x2, y2 = box.xyxy[0]
#             x_center = (x1 + x2) / 2

#             position = get_position(x_center, img_width)

#             detections.append({
#                 "label": label,
#                 "confidence": round(confidence, 2),
#                 "position": position,
#                 "distance": distance
#             })

#     return detections


# def get_distance_label(box_area, img_area):
#     ratio = box_area / img_area

#     if ratio > 0.15:
#         return "very close"
#     elif ratio > 0.05:
#         return "near"
#     else:
#         return "far"



import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

CONFIDENCE_THRESHOLD = 0.5

IMPORTANT_OBJECTS = {
    "person", "chair", "door", "table",
    "car", "bicycle", "bus", "stairs"
}

def get_position(x_center, img_width):
    if x_center < img_width / 3:
        return "left"
    elif x_center < 2 * img_width / 3:
        return "front"
    else:
        return "right"

def get_distance_label(box_area, image_area):
    ratio = box_area / image_area

    if ratio > 0.15:
        return "very close"
    elif ratio > 0.05:
        return "near"
    else:
        return "far"

def detect_objects(image_bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    img_height, img_width, _ = img.shape
    image_area = img_height * img_width

    results = model(img)
    detections = []

    for r in results:
        for box in r.boxes:
            confidence = float(box.conf[0])
            if confidence < CONFIDENCE_THRESHOLD:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label not in IMPORTANT_OBJECTS:
                continue

            x1, y1, x2, y2 = box.xyxy[0]

            # Position
            x_center = (x1 + x2) / 2
            position = get_position(x_center, img_width)

            # Distance
            box_area = (x2 - x1) * (y2 - y1)
            distance = get_distance_label(box_area, image_area)

            detections.append({
                "label": label,
                "confidence": round(confidence, 2),
                "position": position,
                "distance": distance
            })

    return detections
