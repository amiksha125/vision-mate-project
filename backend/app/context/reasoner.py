
# def generate_description(detections):
#     if not detections:
#         return "I do not see any important objects nearby."

#     messages = []

#     for det in detections:
#         label = det["label"]
#         messages.append(f"{label}")

#     unique = list(set(messages))

#     return "I see " + ", ".join(unique) + " around you."



# from models.scene_caption import generate_scene_caption

# def generate_description(detections, image):
#     # Fallback: no detections → scene caption
#     if not detections:
#         caption = generate_scene_caption(image)
#         return f"I see {caption}."

#     # Object-based description
#     sentences = []

#     for det in detections:
#         label = det["label"]
#         position = det["position"]
#         sentences.append(f"There is a {label} on your {position}.")

#     return " ".join(sentences)



# from models.scene_caption import generate_scene_caption

# def generate_description(detections, image):
#     """
#     Generates a human-friendly description of the scene.
#     Priority:
#     1. Important detected objects with spatial context
#     2. Fallback to scene captioning if no objects detected
#     """

#     # Fallback: no objects detected
#     if not detections:
#         caption = generate_scene_caption(image)
#         return f"I see {caption}."

#     sentences = []

#     for det in detections:
#         label = det["label"]
#         position = det["position"]
#         sentences.append(f"There is a {label} on your {position}.")

#     return " ".join(sentences)

from collections import defaultdict
from models.scene_caption import generate_scene_caption

def generate_description(detections, image):
    # Fallback: no detections
    if not detections:
        caption = generate_scene_caption(image)
        return f"I see {caption}."

    position_map = defaultdict(set)

    for det in detections:
        position_map[det["position"]].add(det["label"])

    sentences = []

    for position, labels in position_map.items():
        if len(labels) == 1:
            label = list(labels)[0]
            sentences.append(f"There is a {label} in front of you." if position == "front"
                             else f"There is a {label} on your {position}.")
        else:
            label_list = ", ".join(labels)
            sentences.append(f"There are {label_list} on your {position}.")

    return " ".join(sentences)

