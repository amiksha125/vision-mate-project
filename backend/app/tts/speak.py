# from gtts import gTTS
# import os
# import uuid

# AUDIO_DIR = "static/audio"

# os.makedirs(AUDIO_DIR, exist_ok=True)

# def text_to_speech(text: str) -> str:
#     """
#     Converts text to speech and saves it as an MP3 file.
#     Returns the relative path of the audio file.
#     """

#     filename = f"{uuid.uuid4()}.mp3"
#     filepath = os.path.join(AUDIO_DIR, filename)

#     tts = gTTS(text=text, lang="en")
#     tts.save(filepath)

#     return filepath



# Smart sentence + TTS generation pipeline

from gtts import gTTS
import uuid
import os

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4()}.mp3"
    file_path = os.path.join(AUDIO_DIR, filename)

    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(file_path)

    return file_path
