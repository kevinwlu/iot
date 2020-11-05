# Python example of sending email

import smtplib

from_email = 'GMAIL_ADDRESS'
recipients_list = ['RECIPIENT_EMAIL']
cc_list = []
subject = 'Hello'
message = 'This is a test message.'
username = 'GMAIL_USERNAME'
password = 'GOOGLE_APP_PASSWORD'
server = 'smtp.gmail.com:587'

def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtpserver):
    """
    Sends an e - mail.

    Args:
        from_addr: (str): write your description
        to_addr_list: (list): write your description
        cc_addr_list: (list): write your description
        subject: (str): write your description
        message: (str): write your description
        login: (str): write your description
        password: (str): write your description
        smtpserver: (str): write your description
    """
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
