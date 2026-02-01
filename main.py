import transcribe
import translation_ai
import translation_api
import TTS

lang_in = "en-US" # e.g. en-US | de-DE
lang_out = "de" # e.g. de | en | cn


transcribe_done = transcribe.Recognize_Speech(wav_file="INPUT.wav", language=lang_in)
print(transcribe_done)
# translation = translation_ai.Translate_AI(text=transcribe_done, language=lang_out)
translation = translation_api.Translate_API(text=transcribe_done, language=lang_out)
print(translation)
TTS.TTS_play(text = translation, language=lang_out)