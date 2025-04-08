from Speech import Speech
from CommandHandler import CommandHandler
from sensitive import API_1
# from Lang_Detect import LangDetect

if __name__ == "__main__":
    command_handler = CommandHandler(API_1)
    speech = Speech()


    while True:
        command = speech.listen_for_command()
        if command:
            # lang_detect = LangDetect(command)
            command_handler.handle_command(command)
