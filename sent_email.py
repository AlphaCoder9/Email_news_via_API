import smtplib
import ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'adeelta302@gmail.com'
    password = 'ekxcwbuchlqzqgui'

    receiver = "adeelt7875@gmail.com"
    # Secure Context for sending emails securely
    context = ssl.create_default_context()

    # using with context manager and point to smtplib ssl
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
