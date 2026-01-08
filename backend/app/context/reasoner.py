
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



from models.scene_caption import generate_scene_caption

def generate_description(detections, image):
    """
    Generates a human-friendly description of the scene.
    Priority:
    1. Important detected objects with spatial context
    2. Fallback to scene captioning if no objects detected
    """

    # Fallback: no objects detected
    if not detections:
        caption = generate_scene_caption(image)
        return f"I see {caption}."

    sentences = []

    for det in detections:
        label = det["label"]
        position = det["position"]
        sentences.append(f"There is a {label} on your {position}.")

    return " ".join(sentences)
