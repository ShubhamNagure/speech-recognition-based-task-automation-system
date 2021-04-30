import pyttsx3
import concurrent.futures

class _TTS:

    engine = None
    voices= None
    rate = 150

    def __init__(self):
        self.engine = pyttsx3.init('sapi5', debug=True)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', self.rate)

    def speak(self,text_):
        """
        Takes plain text and pass it to engine to speak that plain text
        :parameter := audio
        :type := String
        :return:
        Human hearable voice 🔊
        """
        self.engine.say(text_)
        self.engine.runAndWait()

    def textToSpeech(text):
        """
        purpose of this method is to hop waiting after speech execution.

        Use only when you don't want to listen events here.
        :return:
        Deletes engine
        """
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 220)
        engine.say(text)
        engine.runAndWait()
        del engine

    def parallel(self,text):
        """
        Create a parallel thread to textToSpeech method and
        uses a pool of at most max_workers threads to execute calls asynchronously

        :return:
        Asynchronous thread
        """

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future_tasks = {executor.submit(_TTS.textToSpeech, text)}
            for future in concurrent.futures.as_completed(future_tasks):
                try:
                    data = future.result()
                except Exception as e:
                    print(e)