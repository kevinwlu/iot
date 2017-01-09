# Python example of sending email

import smtplib

from_email = '<enter-gmail-address>'
recipients_list = ['<enter-recipient-email>']
cc_list = []
subject = 'Hello'
message = 'This is a test message.'
username = '<enter-gmail-username>'
password = '<enter-google-app-password>'
server = 'smtp.gmail.com:587'

def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

# Send email
sendemail(from_email, recipients_list, cc_list, subject, message, username, password, server)
