import smtplib
from email.message import EmailMessage
from text_to_speech_module import speak  # Import the speak function

EMAIL_ADDRESS = "dhruv.y.jadav@gmail.com"
EMAIL_PASSWORD = "dhryjad@1401108828229838"

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def process_email_command():
    try:
        speak("Sure, what should the subject be?")
        subject = listen_for_command()
        speak("What should the body of the email be?")
        body = listen_for_command()
        speak("To whom should I send the email?")
        to_email = listen_for_command()

        send_email(subject, body, to_email)
        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I encountered an error while sending the email.")
