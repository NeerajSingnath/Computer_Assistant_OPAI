import pyttsx3
import speech_recognition as sr

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 200)

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_for_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for command...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, could not recognize what you said.")
                return None
            except sr.WaitTimeoutError:
                print("No command detected, timing out.")
                return None
            except Exception as e:
                print(f"An error occurred while listening: {e}")
                return None