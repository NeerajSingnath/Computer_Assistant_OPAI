import os
import webbrowser
from urllib.parse import quote_plus

class BrowserActions:
    @staticmethod
    def search_and_play_on_youtube(query):
        try:
            print(f"Searching YouTube for: {query}")
            query_encoded = quote_plus(query)
            search_url = f"https://www.youtube.com/results?search_query={query_encoded}"
            print(f"Opening {search_url}")
            webbrowser.open(search_url)
        except Exception as e:
            print(f"An error occurred while searching YouTube: {e}")

    @staticmethod
    def open_brave():
        try:
            os.startfile("C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe")
        except Exception as e:
            print(f"An error occurred while opening Brave: {e}")

    @staticmethod
    def open_vs_code():
        try:
            os.startfile("C:/Users/speed/AppData/Local/Programs/Microsoft VS Code/code.exe")
        except Exception as e:
            print(f"An error occurred while opening VS Code: {e}")

    @staticmethod
    def open_youtube():
        try:
            webbrowser.open("https://youtube.com")
        except Exception as e:
            print("An error occurred while opening Youtube")