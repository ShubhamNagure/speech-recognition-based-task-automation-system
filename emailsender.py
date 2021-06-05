import smtplib, ssl
from TTS import _TTS
from driver import driver
import csv

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

    def createContact(self):

        """It will write contacts to CSV file so that it can be retrived while sending mail
        Details: `nickname`, `emailID`.

        """

        print("Please enter nickname: ")
        nickname = input()
        print("Please enter EmailID: ")
        emailid = input()
        details = [nickname.lower(),emailid.lower()]
        try:
            with open('contacts.csv', 'a+', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(details)
        except:
            print("Something went wrong when adding contact to the file")
        finally:
            file.close()


    def searchContact(self, mouth,ear):
        """Search from CSV with the help of nickname and return that"""
        count = 0
        try:
            mouth.speak("To Whom you want to send mail ?, Please enter a Nickname...")
            nickname = input('Enter Nickname to find :\n')
            email_id =[]
            choosen_mailids =[]
            csv_file = csv.reader(open('contacts.csv', "r"), delimiter=",")
            # loop through the csv list
            for row in csv_file:

                # if current rows 1st index value is equal to input, print that row
                if nickname in row[0]:
                    email_id.insert(count,row[1])
                    # email_id[count] = row[1]
                    count += 1
            print(email_id)
            flag = False

            if  count > 1 :
                mouth.speak(f"I found {count} mailID associated with {nickname} nickname,\
                        Which one should i choose ? ")

                # mouth.speak(f" There are {count} mail ids, \
                # Please pick mail Ids by saying mentioning there place holder number like first or one, Second or Two, And so on")

                def chooseemailidofreceiver():

                    pronoundict = {
                        "first": 0,
                        "one": 0,
                        "1": 0,
                        "second": 1,
                        "two": 2,
                        "three": 2,
                        "third": 2,
                        "four": 3,
                        "fourth": 3,
                        "five": 4,
                        "fifth": 4
                    }

                    noOfMailId=ear.takeCommand()
                    ind = 0
                    if noOfMailId in pronoundict:
                        print("here")
                        val= pronoundict[noOfMailId]
                        print(val)
                        choosen_mailids.insert(ind,email_id[val])
                        print(email_id[val])
                        ind += 1
                        mouth.speak(f"{email_id[val]} is selected successfully, want to add more ? if no say DONE")

                while(count>0):
                    chooseemailidofreceiver()
                    short_res = ear.takeCommand()
                    if "done" in short_res :
                        """Add logic to implement further process"""
                        print("Done")
                        exit()
                        pass
                    elif "add" in short_res :
                        print("Add")
                        chooseemailidofreceiver()
                        print(choosen_mailids)
                        count -= 1

                # for eid in email_id:
                #     print(eid)

            if count == 1:
                mouth.speak(f"{email_id} is selected as receiver , \
                shall I proceed with these? say Yes Or No to cancel")
                response=ear.takeCommand()
                if response =="yes":
                    return email_id
                elif response =="no":
                    mouth.speak("Email sending activity aborted...")

        except Exception as inst:
            print(type(inst))

    def setYourMailBox(self):
        """ Implement dynamic way of setting there mailbox i.e. `mailID`, `password`"""
        pass

    def getCommandAndSet(self, query, mouth):


        if "" in query:
            mouth.speak(f"you said: {query}")


def start():
    mouth = _TTS()
    mouth.speak(f"Email Sending activity is initiated, Please follow the command")
    mouth.speak(f"Hi{driver.user}, whom you want to send mail?")
    ear = driver()
    query=ear.takeCommand()
    obj = EmailSender(465,"smtp.gmail.com", "athapivathapi@gmail.com")
    # obj.send()
    obj.getCommandAndSet(query,mouth)

def test():
    mouth = _TTS()
    ear = driver()
    obj = EmailSender(465, "smtp.gmail.com", "athapivathapi@gmail.com")
    obj.createContact()
    # obj.searchContact(mouth,ear)

if __name__ == '__main__':
    test()