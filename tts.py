from gtts import gTTS
import os

def text_to_speech(summary):
    tts = gTTS(text=summary, lang='hi')
    tts.save("summary.mp3")
    os.system("start summary.mp3")  # For Windows, use appropriate command for other OS
