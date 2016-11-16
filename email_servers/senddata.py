# senddata.py

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message to send
msg = MIMEText('This is the body of the message')
msg['to'] = email.utils.formataddr(('Recipient', 'casey.oneill@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'caseyoneill78@hotmail.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with server
try:
    server.sendmail('caseyoneill78@hotmail.com', ['casey.oneill@gmail.com'], msg.as_string())
finally:
    server.quit()
