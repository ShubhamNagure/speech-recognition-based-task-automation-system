import smtplib, ssl
from TTS import _TTS
from driver import driver
from getpass import win_getpass
import csv,os


class EmailSender:

    def __init__(self,port,smtp_server,sender_email):
        self.port = port  # For SSL
        self.smtp_server = smtp_server
        self.sender_email = sender_email  # Enter your address

    def createContact(self,mouth):

        """It will write contacts to CSV file so that it can be retrieved while sending mail
        Details: `nickname`, `emailID`.

        """

        print("Please enter nickname: ")
        mouth.speak("Please enter nickname")
        nickname = None
        """Check nickname is already used ?"""
        def nicknamechecker():
            nonlocal nickname
            nickname = input().lower()
            nicknamelist =[]
            try:
                csv_file = csv.reader(open('contacts.csv', "r"), delimiter=",")
                count =0
                # loop through the csv list
                for row in csv_file:

                    nicknamelist.insert(count,row[0])
                    count += 1
            except Exception as inst:
                print(type(inst))


            if nickname in nicknamelist:
                mouth.speak(f"{nickname} nickname is already used, try something else")
                mouth.speak("Please enter an another nickname")
                print("Please enter a another nickname: ")
                return nicknamechecker()

        nicknamechecker()
        print("Please enter EmailID: ")
        mouth.speak("Please enter EmailID")
        emailid = input().lower()
        details = [nickname.lower(),emailid.lower()]
        try:
            with open('contacts.csv', 'a+', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(details)
                mouth.speak(f"{details[1]} Id is successfully added to book")
        except:
            print("Something went wrong when adding contact to the file")
            mouth.speak(f"I could not add {details[1]} id , something wrong with file")
        finally:
            file.close()

    def searchContact(self, mouth,ear):
        """Search from CSV with the help of nickname and return that"""
        count = 0
        try:
            mouth.speak("To Whom you want to send mail ?, Please enter a Nickname...")
            nickname = input('Enter Nickname to find :\n').lower()
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

            """If more than   one email id need to choose this logic will execute"""
            if  count > 1 :
                mouth.speak(f"I found {count} mailID associated with {nickname} nickname,\
                        Which one should i choose ? ")

                # mouth.speak(f" There are {count} mail ids, \
                # Please pick mail Ids by mentioning there place holder number like first or one, Second or Two, And so on")

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
                        "4": 3,
                        "five": 4,
                        "fifth": 4
                    }
                    print("************")
                    noOfMailId=ear.takeCommand()
                    ind = 0
                    if noOfMailId in pronoundict:
                        print("here")
                        val= pronoundict[noOfMailId]
                        print(val)
                        """ Checking here that email id if already selected , 
                                               if yes then warn, else continue"""
                        if email_id[val] in choosen_mailids:
                            mouth.speak(f"{email_id[val]} is already selected, please choose another")
                        else:
                            choosen_mailids.insert(ind,email_id[val])
                            print(email_id[val])
                            ind += 1
                            mouth.speak(f"{email_id[val]} is selected successfully...")

                chooseemailidofreceiver()
                lengthofchoosen = 0
                while lengthofchoosen <= count-1 :
                    mouth.speak("want to add more ? if no say DONE")
                    short_res = ear.takeCommand()
                    if "done" in short_res :
                        """Add logic to implement further process"""
                        print("Done")
                        return choosen_mailids

                    elif "add" in short_res :
                        print("Add")
                        mouth.speak("Please say the number ")
                        chooseemailidofreceiver()
                        print(choosen_mailids)
                        lengthofchoosen=len(choosen_mailids)
                        if lengthofchoosen == count:
                            mouth.speak("You have selected all of them, say continue to proceed")
                            print("all selected")
                        return choosen_mailids


            """If only one email id need to choose this logic will execute"""
            if count == 1:
                mouth.speak(f"{email_id} is selected as receiver , \
                shall I proceed with these? say Yes Or No to cancel")
                response=ear.takeCommand()
                if "yes" in response:
                    return email_id
                elif "no" in response:
                    mouth.speak("Email sending activity aborted...")

        except Exception as inst:
            print(inst)

    def setYourMailBox(self,mouth):
        """ Implement dynamic way of setting there mailbox i.e. `mailID`, `password`"""
        # mouth.speak("Self Emailbox configuration initiated...")
        my_mail_id = None

        def emailidchecker():
            mouth.speak("Please register your email Id")
            nonlocal my_mail_id
            my_mail_id = input('Please register your email Id :\n').lower()
            if "@" not in my_mail_id:
                mouth.speak(f"@ is missing in your {my_mail_id}")
            elif "." not in my_mail_id:
                mouth.speak(f" dot is missing in your {my_mail_id}")
            else:
                """ willsave the email Id to csv file"""
                mouth.speak(f" Perfect,  your mail id is set to {my_mail_id}")

                """get password without echoing"""

                mouth.speak("please enter password :")
                pa = win_getpass("Please enter password \
                (password will not echoed):")

                details =[my_mail_id.lower(),pa]
                try:
                    with open('cred.csv', 'a+', newline='') as file:
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(details)
                        mouth.speak(f"{details[0]} Id is successfully set as"
                                    f" your default sender")
                except:
                    print("Something went wrong while saving credentials")
                    mouth.speak(f"I could not add {details[1]} id , something wrong with file")
                finally:
                    file.close()
                print("valid")

        emailidchecker()



    def getCommandAndSet(self,  mouth, receiver, message):
        """get sender credentials from csv , login get test to send"""
        mouth.speak("Handshake initiated with mail server.")
        sendercred= []
        try:
            """get sender creds and be ready"""

            csv_file = csv.reader(open('cred.csv', "r"), delimiter=",")
            count =0
            # loop through the csv list
            for row in csv_file:
                sendercred.insert(count, row[0])
                sendercred.insert(count, row[1])
                count += 1
        except Exception as e:
            print(e)
        finally:
            pass
        self.sender_email=sendercred[1]
        print(self.sender_email)
        self.password= sendercred[0]
        print(self.password)



        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver, message)
            mouth.speak(f"successfully sent to {receiver} ")

        # if "" in query:
        #     mouth.speak(f"you said: {query}")
    def createmessage(self,ear, mouth):
        mouth.speak("What message do you want to send")
        message = ear.takeCommand()
        print(message)
        return message

    # def checkSenderMailIsConf():
    #     try:
    #         with open('cred.csv', 'r', newline='') as file:
    #             content=file.read()
    #             if content is None:
    #                 obj = EmailSender()
    #                 obj.setYourMailBox()
    #             else:
    #                 pass
    #     except:
    #         pass
    #     finally:
    #         pass


def start():
    #First: The SMTP handshake
    #Second: The message transfer
    #Third: Closing the connection
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
    obj = EmailSender(465,"smtp.gmail.com", "athapivathapi@gmail.com")
    try:
        filesize = os.path.getsize("cred.csv")
        print(filesize)
        if filesize == 0:
            print("empty")
            obj.setYourMailBox(mouth)
            mouth.speak("do you want to add new receiver ?")
            resp=ear.takeCommand()
            if "yes" in resp:
                obj.createContact(mouth)
                choosen_mail=obj.searchContact(mouth,ear)
                print(choosen_mail)
                message=obj.createmessage(ear,mouth)
                obj.getCommandAndSet(mouth,choosen_mail,message)
            elif "no" in resp:
                choosen_mail=obj.searchContact(mouth,ear)
                print(choosen_mail)
                message=obj.createmessage(ear,mouth)
                obj.getCommandAndSet(mouth,choosen_mail,message)
        else:
            mouth.speak("do you want to add new receiver ?")
            resp=ear.takeCommand()
            if "yes" in resp:
                obj.createContact(mouth)
                choosen_mail=obj.searchContact(mouth,ear)
                print(choosen_mail)
                message=obj.createmessage(ear,mouth)
                obj.getCommandAndSet(mouth,choosen_mail,message)                
            elif "no" in resp:
                choosen_mail=obj.searchContact(mouth,ear)
                print(choosen_mail)
                message=obj.createmessage(ear,mouth)
                obj.getCommandAndSet(mouth,choosen_mail,message)
    except:
        mouth.speak("Error : Task aborted ")
    

    # # obj.createContact(mouth)
    # choosen_mail=obj.searchContact(mouth,ear)
    # # obj.setYourMailBox(mouth)
    # message=obj.createmessage(ear,mouth)
    # obj.getCommandAndSet(mouth,choosen_mail,message)

if __name__ == '__main__':
    test()