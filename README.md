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


Speech-Based Assistive Feedback

VisionMate is designed for visually impaired users, where textual descriptions alone are insufficient. To ensure real-world usability, the system converts visual scene descriptions into spoken audio feedback.

How it works
* An input image frame is analyzed using YOLOv8 for object detection.
* Detected objects are enriched with spatial context (left, front, right).
* A human-friendly scene description is generated.
* The description is converted into speech using Text-to-Speech (TTS).
* The generated audio file is served via a FastAPI static endpoint.

Why this matters

* Enables hands-free accessibility
* Provides instant auditory awareness
* Forms the foundation for real-time assistive navigation
* Bridges the gap between computer vision and human perception

This speech module is a key step toward making VisionMate a practical assistive system rather than a visual-only application.



## 🔊 Speech Generation Module

The Speech Module converts the generated scene description into audible feedback,
making the system accessible for visually impaired users.

### Why Speech is Important
- Enables real-time environmental awareness
- Reduces dependency on visual interfaces
- Improves safety and navigation assistance

### Workflow
1. Object detection generates spatial descriptions (left, front, right)
2. Redundant detections are filtered to avoid repeated speech
3. A concise natural-language sentence is generated
4. Text-to-Speech (TTS) converts the description into audio output

### Key Features
- Human-friendly, non-repetitive speech
- Context-aware object grouping
- Works in real-time with live camera frames

### Example Output
> "There is a person in front of you and a chair on your left."


“I generate speech dynamically using gTTS.
Each request creates a uniquely named audio file stored in a static directory to prevent cache issues.
The frontend simply plays the returned audio URL.”

“Audio files are generated dynamically with UUID-based filenames and stored under a static directory. This avoids overwriting and caching issues while allowing direct frontend playback.”


“Your audio sounds the same every time”

You say:

“That’s expected. Text-to-speech generates identical audio for identical text.
We use UUID filenames to prevent caching and overwriting, not to alter speech content.”


VisionMate estimates distance using bounding box area relative to image size.
This monocular vision approach avoids depth sensors while still providing
meaningful proximity awareness for users.

VisionMate prioritizes safety by overriding scene narration with danger alerts when a high-risk object is detected very close to the user.