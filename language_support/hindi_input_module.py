# language_support/hindi_input_module.py
import speech_recognition as sr

class HindiInputModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def toggle_hindi(self, on=True):
        if on:
            # Adjust recognizer settings for Hindi language
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = 4000  # Adjust this threshold as needed
            self.recognizer.dynamic_energy_threshold = False
            self.recognizer.pause_threshold = 1.0
            self.recognizer.non_speaking_duration = 0.5
        else:
            # Revert to default settings for English or other languages
            self.recognizer = sr.Recognizer()

    def listen_for_hindi_command(self):
        with sr.Microphone() as source:
            print("सुन रहा हूँ...")  # Inform the user that the assistant is listening in Hindi
            audio = self.recognizer.listen(source, timeout=None)  # Listen indefinitely until speech is detected

        try:
            command = self.recognizer.recognize_google(audio, language="hi-IN")
            print("आपने कहा:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("मुझे समझ में नहीं आया।")
            return ""
        except sr.RequestError as e:
            print("परिणाम प्राप्त करने में समस्या हुई; कृपया अपने नेटवर्क कनेक्शन की जाँच करें:", e)
            return ""
