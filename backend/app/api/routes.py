# from fastapi import APIRouter, UploadFile, File
# from app.vision.detector import detect_objects
# from app.context.reasoner import generate_description

# router = APIRouter()

# @router.post("/analyze-frame")
# async def analyze_frame(file: UploadFile = File(...)):
#     image_bytes = await file.read()
#     detections = detect_objects(image_bytes)
#     description = generate_description(detections)
#     return {"description": description}


from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io

from app.vision.detector import detect_objects
from app.context.reasoner import generate_description

router = APIRouter()

@router.post("/analyze-frame")
async def analyze_frame(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Convert bytes → PIL Image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Detect objects
    detections = detect_objects(image_bytes)

    # 🔴 THIS IS THE FIX (image is passed)
    description = generate_description(detections, image)

    return {
        "description": description,
        "objects_detected": len(detections)
    }

