import speech_recognition as sr

class SpeechRecognition:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, audio):
        print("Transcribing...")
        while True:
            try:
                with sr.AudioFile(audio) as source:
                    audio_data = self.recognizer.record(source)

                    command = self.recognizer.recognize_google(audio_data).lower()
                    return command

            except sr.UnknownValueError:
                print("error")
                return "Error: voice not detected in the audio"
            except sr.RequestError:
                return "Error: Speech service down"
