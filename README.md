# vision-mate-project
VisionMate is an AI-powered assistive system designed to help visually impaired users understand their surroundings through audio-based descriptions.

The backend is responsible for:
Receiving camera frames
Running AI-based object detection
Filtering irrelevant or incorrect detections
Generating meaningful, human-friendly descriptions
This backend is built using FastAPI and follows a modular, scalable architecture.

main.py — Application Entry Point

What it does:
Creates the FastAPI application
Registers all API routes
Starts the backend server


This is the starting point of the backend
Keeps application setup separate from business logic

“This file starts VisionMate’s backend and connects everything together.”

🔹 api/routes.py — API Endpoints

What it does:
Defines backend URLs (endpoints)
Handles incoming requests from frontend
Sends responses back

Example:

/analyze-frame → accepts an image and returns a description

Keeps API logic separate from AI logic
Makes it easy to add new endpoints later
In simple words:

“This file is the communication bridge between the user and the AI system.”

🔹 vision/detector.py — Object Detection Module

What it does:
Loads the YOLOv8 object detection model
Takes an image as input
Detects objects like person, chair, door, etc.

Filters detections using:

Confidence threshold
Important object list

Raw AI models make mistakes
We restrict detection to useful objects only
Improves reliability for visually impaired users

“This file helps the system ‘see’ the environment in a meaningful way.”

🔹 context/reasoner.py — Context & Reasoning Engine

What it does:
Takes detected objects as input
Converts them into natural language sentences
Removes duplicates and unnecessary information

Example:

Raw detection → ["person", "chair"]
Output → “I see a person and a chair around you.”

Why it exists:

AI detection alone is not helpful
Users need clear, calm, and useful explanations

“This file turns AI output into something humans can understand.”

🔹 tts/speak.py — Text-to-Speech Module (Future Use)

What it does:

Converts generated text into audio using TTS
Will allow spoken feedback instead of text

Why it exists:
VisionMate is audio-first
Visually impaired users rely on speech output

(Currently prepared for future integration.)

“This file will allow VisionMate to speak.”

🔹 core/config.py — Configuration File (Scalability)

What it does:
Will store constants and configuration values

Example: thresholds, environment settings

Why it exists:

Avoids hardcoding values
Makes system easier to tune and deploy

“This file keeps important settings in one place.”

🔹 models/ — Model Storage

What it does:

Placeholder for storing trained or fine-tuned models
Prevents clutter in code folders
Clean separation between code and ML assets

# Next Step is to implement left / center / right detection.
Instead of:

“I see a person and a chair.”
VisionMate should say:

“There is a person in front of you. A chair is on your left.”
This is exactly how a visually impaired person thinks spatially.

An image has width.
We divide the image into 3 vertical regions:
|   LEFT   |   CENTER   |   RIGHT   |
YOLO gives bounding boxes like this:
(x1, y1, x2, y2)

object_center_x = (x1 + x2) / 2
