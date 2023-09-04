import datetime
from speech_recognition_module import listen_for_command
from text_to_speech_module import speak
from email_module import process_email_command
from web_search_module import process_search_command
from weather_module import process_weather_command
from calculator_module import add, subtract, multiply, divide
from jokes_module import get_joke
from apps_module import open_app
from ai_writer_module import generate_and_write_text
from reminder_module import set_reminder, check_reminders
import os

def get_time_of_day_greeting():
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        return "Good morning!"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def greet_with_name():
    speak("Hello, what's your name?")
    name = listen_for_command().strip()
    if name:
        speak(f"Hello, {name}! I'm Jarvis, your personal voice assistant.")
        speak("How can I assist you today?")
    else:
        speak("Hello there! I'm Jarvis, your personal voice assistant. What's on your mind?")

def write_to_notepad(text):
    with open("speech_to_text.txt", "a") as file:
        file.write(text + "\n")
    os.system("start notepad speech_to_text.txt")

def process_command(command):
    if "hello" in command:
        personalized_greeting = get_personalized_greeting()
        speak(f"{personalized_greeting} How can I help you?")
    elif "send email" in command:
        process_email_command()
    elif "search" in command:
        process_search_command(command)
    elif "weather" in command:
        process_weather_command(command)
    elif "calculator" in command:
        speak("Sure, I'm ready for calculations. Please provide the operation and numbers.")
        operation = listen_for_command().lower()
        if "add" in operation:
            speak("Please provide the first number.")
            num1 = float(listen_for_command())
            speak("Please provide the second number.")
            num2 = float(listen_for_command())
            result = num1 + num2
        elif "subtract" in operation:
            speak("Please provide the first number.")
            num1 = float(listen_for_command())
            speak("Please provide the second number.")
            num2 = float(listen_for_command())
            result = num1 - num2
        elif "multiply" in operation:
            speak("Please provide the first number.")
            num1 = float(listen_for_command())
            speak("Please provide the second number.")
            num2 = float(listen_for_command())
            result = num1 * num2
        elif "divide" in operation:
            speak("Please provide the numerator.")
            num1 = float(listen_for_command())
            speak("Please provide the denominator.")
            num2 = float(listen_for_command())
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "I'm sorry, I didn't understand that operation."

        speak(f"The result is: {result}")

    elif "set reminder" in command:
        speak("Sure, what should be the name of the reminder?")
        name = listen_for_command().strip()
        speak("When should I remind you? Please provide the date and time in 'YYYY-MM-DD HH:MM:SS' format.")
        time_str = listen_for_command().strip()
        speak("What ringtone would you like? You can say 'default' for the system beep.")
        ringtone = listen_for_command().strip().lower()
        reminder_result = set_reminder(name, time_str, ringtone)
        speak(reminder_result)
    elif "check reminders" in command:
        check_reminders()

        
    elif "write" in command and "in notepad" in command:
        text_to_write = command.replace("write", "").replace("in notepad", "").strip()
        write_to_notepad(text_to_write)
    elif "tell me a joke" in command:
        joke_setup, joke_punchline = get_joke()
        speak(f"Sure, here's a joke for you: {joke_setup}. {joke_punchline}")
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_app(app_name)
    elif "stop 1417 stop" in command:
        speak("Goodbye!")
        exit()  # Terminate the script

    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    while True:
        command = listen_for_command()
        process_command(command)
