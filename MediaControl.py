import time
from pynput.mouse import Controller, Button
import webbrowser

class MediaControl:
    @staticmethod
    def play_on_spotify(command):
        command = command.lower().replace("play ", "").replace(" on spotify", "")
        encoded_query = command.replace(" ", "%20")
        spotify_url = f"https://open.spotify.com/search/{encoded_query}"
        webbrowser.open(spotify_url)
        time.sleep(5)
        target_x, target_y = 720, 463
        mouse = Controller()
        mouse.position = (target_x, target_y)
        time.sleep(1)
        mouse.click(Button.left, 1)