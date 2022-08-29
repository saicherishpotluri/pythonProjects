import email
from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

emailSender = 'sender@email.com'
emailPassword = password

emailReceiver = 'receiver@email.com'

subject = 'Hello, I hope you are doing good'
body = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())