import datetime

def get_personalized_greeting():
    current_time = datetime.datetime.now().time()
    if current_time.hour < 12:
        return "Good morning!"
    elif 12 <= current_time.hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
    