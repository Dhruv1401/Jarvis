# language_support/french_input_module.py
import speech_recognition as sr

class FrenchInputModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def toggle_french(self, on=True):
        if on:
            # Adjust recognizer settings for French language
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 3000  # Adjust this threshold as needed
            self.recognizer.dynamic_energy_threshold = False
            self.recognizer.pause_threshold = 1.0
            self.recognizer.non_speaking_duration = 0.5
        else:
            # Revert to default settings for English or other languages
            self.recognizer = sr.Recognizer()

    def listen_for_french_command(self):
        with sr.Microphone() as source:
            print("J'écoute...")  # Inform the user that the assistant is listening in French
            audio = self.recognizer.listen(source, timeout=None)  # Listen indefinitely until speech is detected

        try:
            command = self.recognizer.recognize_google(audio, language="fr-FR")
            print("Vous avez dit:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Je n'ai pas compris.")
            return ""
        except sr.RequestError as e:
            print("Impossible de récupérer les résultats ; vérifiez votre connexion réseau:", e)
            return ""
