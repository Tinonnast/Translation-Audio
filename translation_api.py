import requests
import json
from translate import Translator

def Translate_API(text, language):
    translator = Translator(to_lang=language) # language e.g.: en | de | fr | cn | hi | ja
    translation = translator.translate(text)
    return translation