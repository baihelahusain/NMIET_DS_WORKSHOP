import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = 'your_email@gmail.com'
    receiver = 'authority_email@example.com'
    password = 'your_app_password'  # Use app-specific password for Gmail

    msg = MIMEText('Vandalism detected at Area X!')
    msg['Subject'] = 'URGENT: Vandalism Alert'
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
