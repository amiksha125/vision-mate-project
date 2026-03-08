from fastapi import FastAPI
from app.api.routes import router
from fastapi.staticfiles import StaticFiles
from app.api.routes import router as analyze_router
from app.api.stream_route import router as stream_router

app = FastAPI(
    title="VisionMate API",
    description="AI Assistant for Visually Impaired",
    version="1.0"
)

app.include_router(router)

# stream route to receive frames

app.include_router(analyze_router)
app.include_router(stream_router)

@app.get("/")
def root():
    return {"message": "VisionMate backend is running"}

app.mount("/static", StaticFiles(directory="static"), name="static")