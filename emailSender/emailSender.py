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
I am a graduate student pursuing my Masters in Computer Science, with a GPA of 3.67/4.0
from Arizona State University, at Tempe. I have a bachelor's degree in Computer Science and
I have experience with Python, Java, and SQL. I am very much interested in data analytics and
I also like making applications. I am confident and self-driven and I have an insatiable desire
to learn. I like solving problems and I am a team player.
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