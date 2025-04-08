from Speech import Speech
from AIInteraction import AIInteraction
from BrowserActions import BrowserActions
from MediaControl import MediaControl


class CommandHandler:
    def __init__(self, api_key):
        self.speech = Speech()
        self.ai = AIInteraction(api_key)
        self.browser = BrowserActions()
        self.media = MediaControl()

    def handle_command(self, text):
        if "gama" in text:
            if "go up" in text:
                self.speech.text_to_speech("Going up")
            elif "go down" in text:
                self.speech.text_to_speech("Going down")
            elif "go right" in text:
                self.speech.text_to_speech("Going right")
            elif "go left" in text:
                self.speech.text_to_speech("Going left")
        elif "play" in text and "on youtube" in text:
            song = text.replace("play", "").replace("on youtube", "").strip()
            self.browser.search_and_play_on_youtube(song)
        elif "play" in text and "on spotify" in text:
            self.media.play_on_spotify(text)
        elif "open youtube" in text:
            self.speech.text_to_speech("Opening YouTube")
            self.browser.open_youtube()
        elif "exit" in text:
            self.speech.text_to_speech("Goodbye! Thank you for using me.")
            exit()
        elif "open brave" in text:
            self.browser.open_brave()
        elif "open vs code" in text:
            self.browser.open_vs_code()
        else:
            answer = self.ai.ask_openai(text)
            self.speech.text_to_speech(answer)