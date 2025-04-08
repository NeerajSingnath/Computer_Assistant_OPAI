from langdetect import detect
from googletrans import Translator

class LangDetect:
    def __init__(self, text):
        self.language = detect(text)
        self.text = text
        self.translator = Translator()

    def translate_to_english(self):
        translated = self.translator.translate(self.text, src=self.language, dest='en')
        print(f"Detected language: {self.language}")
        print(f"Translated text: {translated.text}")