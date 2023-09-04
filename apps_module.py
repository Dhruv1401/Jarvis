import os

def open_app(app_name):
    if "chrome" in app_name:
        os.system("start chrome")
    elif "notepad" in app_name:
        os.system("start notepad")
    # Add more app names and corresponding commands as needed
    else:
        return "I'm sorry, I don't know how to open that app."
