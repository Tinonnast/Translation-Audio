import speech_recognition as sr

def Recognize_Speech(wav_file, language):
    Recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio = Recognizer.record(source)

    return Recognizer.recognize_google(audio, language=language) # language e.g. - en-US | de-DE