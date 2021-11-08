# Speech-Recognition-Based-Task-Automation-System
Day to day task automated by using speech recognition module.


# 1) Weather

## Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```

Cli used to gather weather information. It is a basic wrapper around [wttr.in](http://wttr.in/)'s http interface.

```shell
user@computer:~$ python3 weather.py
Venice, Italy

      \   /     Sunny
       .-.      10 °C          
    ― (   ) ―   ↖ 0 km/h       
       `-’      10 km          
      /   \     0.0 mm         
```

Use the ```--help``` option to learn all the options available.

### Dependencies
* [Requests](https://requests.readthedocs.io/)
* [Click](https://click.palletsprojects.com/)

# 2) Autotyper

## Requirements

First thing first, you must have [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) installed.

### Setup and activate virtual environment :
For Unix based systems please execute the following command to create venv and install requirements.
```
make init
source .venv/bin/activate
```
For windows user, 
```
py -m venv env
.\env\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```


## How to use
Just stretch over image, it will type on prescribed point

* Press Up key : For defining particular page
* Press Click : At (0,0) of your image for initialization
* Press Click : At (x,y) of your image for coordinates termination
* Press Down Key : For defining typing part

## Examples
### First
<div align="center">
  <img src="GIF/auto_typer_eg-1.gif"/>
</div>

## Second
<div align="center">
  <img src="GIF/auto_typer_eg-2.gif"/>
</div>

# 3) EmailSender

EmailSender a command line script and module to sending email. Using either as 
a command line script or importing as a module in another python script/program 

When using EmailSender you can send an email to any recipient using a local 
or remote SMTP server including authentication. Please consider security for
your local system when using.

## Requirements
* Python 3

## Usage as a command line script

The command line script has a number of options, some of which are required 
and some which are not.

```bash
usage: email_sender.py [-h] [--subject SUBJECT] [--from_email FROM_EMAIL] [--to_email TO_EMAIL] [--message MESSAGE]
              [--host HOST] [--port PORT] [--starttls] [--ssl] [--username USERNAME] [--password PASSWORD]

EmailSender

optional arguments:
  -h, --help            show this help message and exit
  --subject SUBJECT     Subject to use in the Email message
  --from_email FROM_EMAIL
                        Email address to use as the from address.
  --to_email TO_EMAIL   Email address to used to send emails too.
  --msg MESSAGE     Email message
  --host HOST           SMTP Host
  --port PORT           SMTP Port
  --username USERNAME   SMTP username
  --password PASSWORD   SMTP password
```

When running as a command line script we have two sets of options, options for 
SMTP/Authentication and then the email message options.

#### Examples

* ***Sending an email to a local SMTP server without any authentication***

```bash
python email_sender.py --subject "Test Email" --from_email sam@example.com --to_email tom@example.com
```

* ***Sending an email using Gmail***

You can specify the smtp host/port along with the username/password if required by the smtp server.

```bash
python app.py --subject test-sunday-1 --from_email sam@gmail.com --to_email tom@gmail.com --host smtp.gmail.com --port 587 --username sam@gmail.com --password PASSWORD
```

## Usage as a Module

You can use this in your own code

```python
from email_sender.email_sender import EmailSender

# setup the object
email_sender = EmailSender()

# send an email
email_sender.send_email(subject="Test Email",
                        from_email=sam@example.com,
                        to_email=tom@example.com,
                        msg="This is a test email")
```

