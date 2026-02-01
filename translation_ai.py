from google import genai

def Translate_AI(text, language): 
    client = genai.Client(api_key="AIzaSyCqtq0qEgQvauuc9dDjWWIFh1VAdQhzeng")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=f"Translate the message \"{text}\" to the language {language} without changing the content or answering questions. Translate the text so the Text has the same meaning in both languages and can be understood in the translated language well" # Change if needed
    )

    return response.text()