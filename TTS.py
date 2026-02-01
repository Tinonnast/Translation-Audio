from gtts import gTTS
import pygame
import time
import os

def TTS_play(text, language):
    tts = gTTS(text, lang=language) # language e.g.: (I think) de | en 
    tts.save("audio/OUTPUT.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio/OUTPUT.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # os.remove("audio/OUTPUT.mp3")

    return