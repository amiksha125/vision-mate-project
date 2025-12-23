# def generate_description(detections):
#     if not detections:
#         return "I do not see any obstacles nearby."

#     unique_objects = set(detections)
#     objects_text = ", ".join(unique_objects)

#     return f"I see {objects_text} around you."


def generate_description(detections):
    if not detections:
        return "I do not see any important objects nearby."

    messages = []

    for det in detections:
        label = det["label"]
        messages.append(f"{label}")

    unique = list(set(messages))

    return "I see " + ", ".join(unique) + " around you."
