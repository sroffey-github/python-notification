import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv() # loads env variables

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

def send_mail(email, password, FROM, TO, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(email, password)

    server.sendmail(FROM, TO, msg.as_string())
    server.quit()

FROM = email

TO   = "example@example.com"

subject = "Example Subject"

msg = MIMEMultipart("alternative")

msg["From"] = FROM

msg["To"] = TO

msg["Subject"] = subject

text = """
This email is sent using Python!
"""

text_part = MIMEText(text, "plain")

msg.attach(text_part)

# send the mail
send_mail(email, password, FROM, TO, msg)