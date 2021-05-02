import smtplib, ssl
from TTS import _TTS
from driver import driver


class EmailSender:


    def __init__(self,port,smtp_server,sender_email):
        self.port = port  # For SSL
        self.smtp_server = smtp_server
        self.sender_email = sender_email  # Enter your address





    def send(self):
        self.receiver_email = "shubhamnagure2344@gmail.com"  # Enter receiver address
        self.password = input("Type your password and press enter: ")


        message = """\
            Subject: Hi there

            This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message)

    def getCommandAndSet(self):
        pass

def start():
    mouth = _TTS()
    mouth.speak(f"Email Sending activity is initiated, Please follow the my command")

    ear = driver()
    receiver=ear.takeCommand()
    obj = EmailSender(465,"smtp.gmail.com", "athapivathapi@gmail.com")
    obj.send()

if __name__ == '__main__':
    start()