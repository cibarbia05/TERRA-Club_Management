import smtplib, ssl
from email.message import EmailMessage


def send_mail(sender_email, sender_password, receiver_email, subject, message):
    msg = EmailMessage()
    print(subject)

    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    print(sender_email)
    print(sender_password)

    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
