import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    data = response.json()
    return data["setup"], data["punchline"]
