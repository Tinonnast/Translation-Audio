<h1>Translation-Audio</h1>
Simple .WAV Speech Recognizer with Translation.<br><br>
Add .WAV File to /audio as INPUT.wav or which name you gave it in the script.<br>
Saves a File to /audio/OUTPUT.mp3 with the translated TTS of your message.<br><br>
Automatically plays the mp3 using pygame.<br><br><br>

<h2>Needed pip installs</h2><br>
pip install pygame gTTS speech-recognition-fork translate<br>
OPTIONAL (for AI Translate): pip install google-genai<br><br>
<h2>AI Translate</h2><br>
Uses Google's Gemini API. Please add your API Key in line 4 of translation_ai.py to use it.<br>
Get a (limited) free API Key at https://aistudio.google.com/api-keys<br><br>
