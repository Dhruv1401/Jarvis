import requests
from bs4 import BeautifulSoup
from text_to_speech_module import speak  # Import the speak function

def get_weather(city):
    BASE_URL = f"https://www.google.com/search?q=weather+in+{city}"
    
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        weather_text = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
        return f"The weather in {city} is {weather_text}."
    except AttributeError:
        return "Sorry, I couldn't fetch the weather information."

def process_weather_command(command):
    try:
        city = command.replace("weather", "").strip()
        weather_info = get_weather(city)
        speak(weather_info)
    except Exception as e:
        speak("Sorry, I encountered an error while fetching the weather information.")
