import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import socket
from TTS import _TTS
import auto_typer


class driver:

    @staticmethod
    def wishMe(tts):
        """
        Just Greetings ...
        :parameter := None
        :return: := None
        """
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            tts.speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            tts.speak("Good Afternoon!")

        else:
            tts.speak("Good Evening!")

        tts.speak("I am Jarvis Sir. Please tell me how may I help you")

    @staticmethod
    def takeCommand():
        """
        It takes microphone input from the user and returns string output
        :return:

        returns string query
        """

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 200
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

    """Main Execution starts from here"""

    def handle(query,tts) :
        """
        Summary or Description of the Function
        :Logic for executing tasks based on query

        :parameter - Query (From the command)
        :type - String

        :return:
        return nothing
        """
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            tts.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            tts.speak("According to Wikipedia")
            print(results)
            tts.speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # TODO: change path or implement API for music
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            tts.speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\r\\AppData\\" \
                       "Local\\Programs\\Microsoft VS Code\\Code.exe"
            # "C:\Users\r\AppData\Local\Programs\Microsoft VS Code\bin"
            os.startfile(codePath)

        elif 'weather' in query:

            tts.speak("Let me see how the weather is ?")
            # with open("weather.py") as f:
            #     code = compile(f.read(), "weather.py", 'exec')
            #     exec(code)
            os.system('python weather.py')
            tts.speak("Weather is populated on terminal ! "
                         "please check")

        elif 'typer' in query:
            auto_typer.start(0.01)

        elif 'goodbye' in query:
            user = socket.gethostname()
            tts.speak(f"See you again {user}")
            exit()


def start():
    tts = _TTS()
    driver.wishMe(tts)
    while True:
        query: str = driver.takeCommand().lower()
        driver.handle(query, tts)


if __name__ == '__main__':
    start()
