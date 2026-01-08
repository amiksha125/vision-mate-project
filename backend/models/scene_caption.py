# from transformers import BlipProcessor, BlipForConditionalGeneration
# from PIL import Image

# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# def generate_scene_caption(image: Image.Image) -> str:
#     inputs = processor(image, return_tensors="pt")
#     output = model.generate(**inputs, max_new_tokens=30)
#     caption = processor.decode(output[0], skip_special_tokens=True)
#     return caption


from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

def generate_scene_caption(image: Image.Image) -> str:
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption
