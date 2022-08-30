import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.encoders import encode_base64
from getpass import getpass
#password = getpass()

SUBJECT = "Email Data"

msg = MIMEMultipart()
msg['Subject'] = 'teste de attach' 
msg['From'] = ''
msg['To'] = ''

part = MIMEBase('application', "octet-stream")
part.set_payload(open("running-out-template.pdf", "rb").read())
encode_base64(part)
    
part.add_header('Content-Disposition', 'attachment; filename="running-out-template.pdf"')

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login('', '')

server.sendmail('', '', msg.as_string())
# avndvcafhlfaqxea