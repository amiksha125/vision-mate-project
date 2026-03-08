from fastapi import APIRouter
import cv2
import base64
import numpy as np
from PIL import Image
import io

from app.vision.detector import detect_objects
from app.context.reasoner import generate_description
from app.tts.speak import text_to_speech

router = APIRouter()

@router.post("/analyze-frame-stream")
async def analyze_frame_stream(frame: str):
    
    # Decode base64 frame
    img_bytes = base64.b64decode(frame)
    image = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    # Detection
    detections = detect_objects(img_bytes)

    # Reasoning
    description = generate_description(detections, image)

    # Speech
    audio_path = text_to_speech(description)

    return {
        "description": description,
        "audio_url": f"/{audio_path}",
        "objects_detected": len(detections)
    }