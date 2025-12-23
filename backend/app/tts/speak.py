from gtts import gTTS

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
