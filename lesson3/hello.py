import smtplib
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

from_email = 'GMAIL_ADDRESS'
receipients_list = ['RECIPIENT_EMAIL']
cc_list = []
subject = 'Hello'
message = 'Switch pressed on Raspberry Pi'
username = 'GMAIL_USERNAME'
password = 'GOOGLE_APP_PASSWORD'
server = 'smtp.gmail.com:587'

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

def sendmail(from_addr, to_addr_list, cc_addr_list,
             subject, message,
             login, password,
             smtpserver):

    header = 'From: %s \n' % from_addr
    header += 'To: %s \n' % ','.join(to_addr_list)
    header += 'Cc: %s \n' % ','.join(cc_addr_list)
    header += 'Subject: %s \n \n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

while True:
    try:
        if (GPIO.input(25) == True):
            sendmail(from_email, receipients_list,
                     cc_list, subject, message,
                     username, password, server)
        sleep(.01)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
