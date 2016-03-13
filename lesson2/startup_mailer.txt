Source: http://elinux.org/RPi_Email_IP_On_Boot_Debian
pi@raspberrypi ~ $ sudo nano /etc/rc.local
#!/bin/sh -e
# 
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address 
sleep 30
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
 printf "My IP address is %s\n" "$_IP"
 python /home/pi/startup_mailer.py        <<<------------------------------------------ ADD THIS LINE!!!
fi

exit 0
