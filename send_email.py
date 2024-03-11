import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_email(subject, body):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("PASSWORD")
    #print(f"Password: {password}")  # Add this line for debugging
    username = "marcfeitosa1@gmail.com"

    receiver = "marcfeitosa1@gmail.com"

    # Create the MIMEText object with UTF-8 encoding
    message = MIMEMultipart()
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    message["Subject"] = subject

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.as_string())

