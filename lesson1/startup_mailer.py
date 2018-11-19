__author__ = 'Cody Giles'
__license__ = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
__version__ = "1.0"
__maintainer__ = "Cody Giles"
__status__ = "Production"

import subprocess
import smtplib
from email.mime.text import MIMEText
#import datetime

def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, returns the corresponding
    internet connection type as a string, e.g., 'Ethernet.'
    """
    if b'wlan0' in word_list or b'wlan1' in word_list:
        con_type = 'Wi-Fi'
    elif b'eth0' in word_list:
        con_type = 'Ethernet'
    else:
        con_type = 'current'
    return con_type

# Change to your own account information
# Account Information
to = 'RECIPIENT_EMAIL' # Email to send to
gmail_user = 'GMAIL_USERNAME' # Email to send from (MUST BE GMAIL)
gmail_password = 'GOOGLE_APP_PASSWORD' # 16-digit Google App Password if using 2-Step Verification
# that needs a 6-digit verification code to sign in Google Account
# https://www.google.com/landing/2step/help.html 
# If not using 2-Step Verification, it's required to turn on access for "less secure apps"
# https://www.google.com/settings/security/lesssecureapps
# My Account > Sign-in & security > Connected apps & sites > Allow less secure apps: ON
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
#today = datetime.date.today()  # Get current time/date

arg='ip route list'  # Linux command to retrieve IP addresses
# Runs 'arg' in a 'hidden terminal'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'

# Split IP text block into three, and divide the two containing IP addresses into words
ip_lines = data[0].splitlines()
split_line_a = ip_lines[1].split()
#split_line_b = ip_lines[2].split()

# con_type variables for the message text, e.g., 'Ethernet,' 'Wi-Fi,' etc.
ip_type_a = connect_type(split_line_a)
#ip_type_b = connect_type(split_line_b)

"""Because the text 'src' is always followed by an IP address,
we can use the 'index' function to find 'src' and add one to
get the index position of our IP address.
"""
ipaddr_a = (split_line_a[split_line_a.index(b'src')+1]).decode()
#ipaddr_b = (split_line_b[split_line_b.index(b'src')+1]).decode()

# Creates a sentence for each IP address
my_ip_a = 'HOSTNAME %s IP address is %s' % (ip_type_a, ipaddr_a)
#my_ip_b = 'RaspberryPi %s IP address is %s' % (ip_type_b, ipaddr_b)

# Creates the text, subject, 'from', and 'to' of the message
#msg = MIMEText(my_ip_a + "\n" + my_ip_b)
msg = MIMEText(my_ip_a)
#msg['Subject'] = 'IP addresses for RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['Subject'] = 'IP address for HOSTNAME'
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server
smtpserver.quit()
