from PIL import ImageGrab
from pytesseract import pytesseract
import time
import pynput.mouse as ms
import pynput.keyboard as kb
from pynput.keyboard import Key, Controller
from TTS import _TTS


keyboard = Controller()

pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


class AutoTyper:

    clickCount = 0
    pCords = [0, 0, 0, 0]
    defined = False
    pImage = None

    def area_select():
        tts.parallel("Please click Starting point and end point")

        print('Click twice to define TEXT window')


        def on_click(x, y, button, pressed):
            if pressed:
                print('({0}, {1})'.format(x, y))
                if AutoTyper.clickCount == 0:
                    AutoTyper.pCords[0] = x
                    AutoTyper.pCords[1] = y
                elif AutoTyper.clickCount == 1:
                    AutoTyper.pCords[2] = x
                    AutoTyper.pCords[3] = y
                    AutoTyper.defined = True
                    print('')
                    AutoTyper.clickCount = 0
                    return False
                AutoTyper.clickCount += 1

        with ms.Listener(on_click=on_click) as listener:
            listener.join()

    def keyPress():
        tts.speak("Please navigate to TEXT window and press arrow up key from the keyboard ")
        print('UP ARROW')

        def on_press(key):
            i = 10
            print(i)

        def on_release(key):

            if key == Key.up:
                print('Pressed\n')

                AutoTyper.area_select()
                AutoTyper.capture()

                return False

        with kb.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def startTyping(delaytime: float):

        tts.speak("Please navigate to where you want me to start typing...  ")
        tts.speak("Example... Notepad or wordpad ")
        tts.speak("Now press the Arrow down key from keyboard")
        print('DOWN ARROW')

        def on_press(key):
            i = 10
            print(i)

        def on_release(key):
            if key == Key.down:
                print('Pressed\n')
                AutoTyper.output(delaytime)
                return False

        with kb.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def capture():

        if AutoTyper.defined:
            AutoTyper.pImage = ImageGrab.grab(bbox=(AutoTyper.pCords[0],
                                                    AutoTyper.pCords[1],
                                                    AutoTyper.pCords[2],
                                                    AutoTyper.pCords[3]))

        else:
            print('please define an area to OCR before trying to print')

    def output(delaytime: float):

        try:
            paraString = pytesseract.image_to_string(AutoTyper.pImage)
        except SystemError:
            print('\n Error while processing your image, please retry.')
            return False

        length = len(paraString)

        for i in range(length):
            keyboard.press(paraString[i])
            keyboard.release(paraString[i])
            time.sleep(delaytime)


def start(delaytime: float):
    global tts
    tts= _TTS()
    print(tts)
    tts.speak("AutoTyper Initiated, Please follow command ...")
    AutoTyper.keyPress()
    AutoTyper.startTyping(delaytime)


if __name__ == '__main__':
    start(0.01)
