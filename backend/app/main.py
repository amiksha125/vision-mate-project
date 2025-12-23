from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="VisionMate API",
    description="AI Assistant for Visually Impaired",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "VisionMate backend is running"}
