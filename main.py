import transcribe
import translation_ai
import translation_api
import TTS

lang_in = "en-US" # e.g. en-US | de-DE
lang_out = "de" # e.g. de | en | cn
use_ai = False
wav_file = "audio/INPUT.wav"

transcribe_done = transcribe.Recognize_Speech(wav_file=wav_file, language=lang_in)
print(transcribe_done)
if use_ai:
    translation = translation_ai.Translate_AI(text=transcribe_done, language=lang_out)
else:
    translation = translation_api.Translate_API(text=transcribe_done, language=lang_out)

print(translation)
TTS.TTS_play(text = translation, language=lang_out)