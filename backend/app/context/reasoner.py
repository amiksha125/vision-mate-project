

# from collections import defaultdict
# from models.scene_caption import generate_scene_caption

# def generate_description(detections, image):
#     # Fallback: no detections
#     if not detections:
#         caption = generate_scene_caption(image)
#         return f"I see {caption}."

#     position_map = defaultdict(set)

#     for det in detections:
#         position_map[det["position"]].add(det["label"])

#     sentences = []

#     for position, labels in position_map.items():
#         if len(labels) == 1:
#             label = list(labels)[0]
#             sentences.append(f"There is a {label} in front of you." if position == "front"
#                              else f"There is a {label} on your {position}.")
#         else:
#             label_list = ", ".join(labels)
#             sentences.append(f"There are {label_list} on your {position}.")

#     return " ".join(sentences)


from collections import defaultdict
from models.scene_caption import generate_scene_caption

def generate_description(detections, image):
    # Fallback: no detections
    if not detections:
        caption = generate_scene_caption(image)
        return f"I see {caption}."

    # Group by (position, distance)
    scene_map = defaultdict(set)

    for det in detections:
        key = (det["position"], det["distance"])
        scene_map[key].add(det["label"])

    sentences = []

    for (position, distance), labels in scene_map.items():
        label_list = ", ".join(labels)

        if position == "front":
            sentences.append(
                f"There is {label_list} {distance} in front of you."
            )
        else:
            sentences.append(
                f"There is {label_list} {distance} on your {position}."
            )

    return " ".join(sentences)
