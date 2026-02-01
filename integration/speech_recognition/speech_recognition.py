import speech_recognition as sr

class voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, audio):
        print("Transcribing...")
        while True:
            try:
                with sr.AudioFile(audio) as source:
                    #audio = self.recognizer.listen(source)
                    #command = self.recognizer.recognize_google(audio).lower()
                    audio_data = self.recognizer.record(source)

                    command = self.recognizer.recognize_google(audio_data).lower()
                    return command
                    # if command == 'exit':
                    #     print('Exiting...')
                print(command)
            except sr.UnknownValueError:
                print("error")
                return "Error: Speech service down"
            except sr.RequestError:
                return "Error: Speech service down"
