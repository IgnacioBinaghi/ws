import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv

port = 465
email_server = 'smtp.gmail.com'

# load the environment variables (returns current folder of python file)
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir/ ".env"
load_dotenv(envars)

# read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_newsubemail(subject, receiver_email, 
               ):
    # create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("wsAlpha", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        """
    )
    # add the HTML version. This converts the message into a multipart/alternative 
    # container, with the original text message of the first part and the
    # new html message as the second part. 
    msg.add_alternative(
        f"""\
        <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="newsletter.css" rel="stylesheet">
            <title>Template</title>
        </head>
        <body style="position:absolute;
                        border-radius: 25px;
                        border: 2px solid #35852c;
                        background: #ffffff;
                        padding: 20px;
                        left:50%;
                        transform: translate(-50%);
                        margin:0;
                        overflow-x:hidden;">
            <p>Thank You for Joining</p>
        </body>
    </html>
    """,
        subtype="html"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(email_server, port, context=context) as server:
        server.login(sender_email, password_email)
        server.send_message(msg)

'''
if __name__ == "__main__":
    send_email(
        receiver_email="thomasbinaghi@gmail.com",
        subject="Thank You for joining wsAlpha!",        
    )
'''

def send_dupesubemail(subject, receiver_email, 
               ):
    # create the base text message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("wsAlpha", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        """
    )
    # add the HTML version. This converts the message into a multipart/alternative 
    # container, with the original text message of the first part and the
    # new html message as the second part. 
    msg.add_alternative(
        f"""\
        <!DOCTYPE html>

    <html lang="en">
        <head>
            <link href="newsletter.css" rel="stylesheet">
            <title>Template</title>
        </head>
        <body style="position:absolute;
                        border-radius: 25px;
                        border: 2px solid #35852c;
                        background: #ffffff;
                        padding: 20px;
                        left:50%;
                        transform: translate(-50%);
                        margin:0;
                        overflow-x:hidden;">
            <p>Your Account Has Been Updated</p>
        </body>
    </html>
    """,
        subtype="html"
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(email_server, port, context=context) as server:
        server.login(sender_email, password_email)
        server.send_message(msg)

'''
if __name__ == "__main__":
    send_email(
        receiver_email="thomasbinaghi@gmail.com",
        subject="Thank You for joining wsAlpha!",        
    )
'''