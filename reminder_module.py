import datetime
import time
import winsound

# Store reminders in a list
reminders = []

def set_reminder(name, time_str, ringtone):
    try:
        reminder_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        reminders.append((name, reminder_time, ringtone))
        return f"Reminder '{name}' set for {reminder_time}."
    except ValueError:
        return "Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS'."

def check_reminders():
    now = datetime.datetime.now()
    for reminder in reminders:
        name, reminder_time, ringtone = reminder
        if now >= reminder_time:
            print(f"Reminder: {name}")
            play_ringtone(ringtone)
            reminders.remove(reminder)

def play_ringtone(ringtone):
    if ringtone == "default":
        # Default system beep
        winsound.Beep(1000, 2000)
    else:
        # Add custom ringtone logic here
        pass
