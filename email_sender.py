import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from getpass import getpass


def send_email_with_attach(from_email, to_email, file):
    msg = MIMEMultipart()
    msg['Subject'] = 'Report'
    msg['From'] = from_email
    msg['To'] = to_email

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(file))

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(from_email, getpass())

    server.sendmail(from_email, to_email, msg.as_string())
