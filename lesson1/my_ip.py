import socket
import smtplib
from email.mime.text import MIMEText

to = 'RECIPIENT_EMAIL' # Email to send to
gmail_user = 'GMAIL_USERNAME' # Email to send from (MUST BE GMAIL)
gmail_password = 'GOOGLE_APP_PASSWORD' # 16-digit Google App Password required for 2-Step Verification
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use
smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server

ipaddr = socket.gethostbyname(socket.gethostname())

# Creates a sentence for each IP address
my_ip = 'RaspberryPi IP address is %s' % ipaddr

# Creates the text, subject, 'from', and 'to' of the message
msg = MIMEText(my_ip)
msg['Subject'] = 'IP address for RaspberryPi'
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server
smtpserver.quit()
