# user_profiles_module.py
class UserProfile:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.voice_sample = None  # Store the voice sample
        self.additional_info = {}  # Store additional user information

    def update_preferences(self, new_preferences):
        self.preferences.update(new_preferences)

    def set_voice_sample(self, voice_sample):
        self.voice_sample = voice_sample

    def recognize_voice(self, voice_sample):
        # Implement voice recognition logic, e.g., compare voice_sample to the stored voice sample
        # Return True if the voice matches, False otherwise
        pass

    def add_additional_info(self, key, value):
        self.additional_info[key] = value

    def get_additional_info(self, key):
        return self.additional_info.get(key)

    def get_all_additional_info(self):
        return self.additional_info
