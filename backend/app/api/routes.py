from fastapi import APIRouter, UploadFile, File
from app.vision.detector import detect_objects
from app.context.reasoner import generate_description

router = APIRouter()

@router.post("/analyze-frame")
async def analyze_frame(file: UploadFile = File(...)):
    image_bytes = await file.read()
    detections = detect_objects(image_bytes)
    description = generate_description(detections)
    return {"description": description}
