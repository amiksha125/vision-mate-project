

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

DANGER_OBJECTS = {
    "person", "car", "bus", "bicycle", "stairs"
}

def generate_description(detections, image):
    # 🚨 Step 1: Danger alert check
    for det in detections:
        if (
            det["label"] in DANGER_OBJECTS
            and det["distance"] == "very close"
        ):
            position = det["position"]
            label = det["label"]

            if position == "front":
                return f"Warning! {label} very close in front of you. Please be careful."
            else:
                return f"Warning! {label} very close on your {position}. Please be careful."

    # 🟡 Step 2: Fallback to normal reasoning
    if not detections:
        caption = generate_scene_caption(image)
        return f"I see {caption}."

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

