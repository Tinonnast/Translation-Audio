from gtts import gTTS
import pygame
import time

def TTS_play(text, language):
    tts = gTTS(text, lang=language) # language e.g.: (I think) de | en 
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    return