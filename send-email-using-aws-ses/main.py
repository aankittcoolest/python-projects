import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

from email.message import EmailMessage

def send_mail(from_email,to_email, subject, message):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(message)
    print(msg)

    server = smtplib.SMTP(os.getenv("SMTP_SERVER"), port='587')
    server.set_debuglevel(1)
    server.starttls()
    print(os.getenv("ADMIN_USERNAME"))
    print(os.getenv("ADMIN_PASSWORD"))

    server.login(os.getenv("ADMIN_USERNAME"), os.getenv("ADMIN_PASSWORD"))
    server.send_message(msg)
    server.quit()
    print("successfully sent message")


send_mail(os.getenv("FROM_EMAIL"), os.getenv("TO_EMAIL"),"Test subject", "Test body")

