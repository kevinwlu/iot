# <a href="https://goo.gl/4aXo9L">Lesson 1</a>: Overview

# Download the New Out Of Box Software (NOOBS) in ZIP at https://www.raspberrypi.org/downloads/noobs

# Extract the NOOBS ZIP file to a folder and select all items in the folder

# Copy all items to a 32GB micro Secure Digital High Capacity (SDHC) memory card

# Insert the microSDHC memory card to a Raspberry Pi

# Connect the Raspberry Pi to a HDMI monitor, and USB keyboard and mouse

# Connect the Raspberry Pi to a micro-USB 5V 2.5A power supply

# Click "Wi-Fi network," select network, and enter username and password

# Select "Raspbian" and "English (US) Language and Keyboard," click "Install" and "OK"

# Click "OK" to reboot after "OS(es) Installed Successfully"

# Click "Next" to set country and change password

# Skip Wi-Fi Network and Updates

# Reboot again

# Pull down the Raspberry Pi menu, and select "Preferences" and "Raspberry Pi Configuration"

# Change Hostname, disable "Auto Login," and enable "Wait for network" under the "System" tab

# Enable SSH/VNC/SPI/I2C/Serial Port, and disable Serial Console under the "Interfaces" tab

# Click "OK" and reboot

# Open a command-line interface (CLI) Terminal

# Clone IoT repository from GitHub

git clone https://github.com/kevinwlu/iot.git

# Copy startup_mailer.py to the current directory "."

cp ~/iot/lesson1/startup_mailer.py .

# Open a Chromium browser and go to https://myaccount.google.com

# Click "Sign-in & security" and turn on 2-Step Verification

# Select a second verification step with "Authenticator app"

# Generate a 16-digit "App password" with the app as "Mail" and device as "Raspberry Pi" 

# Edit startup_mailer.py by changing RECIPIENT_EMAIL, GMAIL_USERNAME, GOOGLE_APP_PASSWORD, and HOSTNAME

nano startup_mailer.py

# Edit /etc/rc.local as in startup_mailer.txt

sudo nano /etc/rc.local

# Set up Wi-Fi as in wpa_supplicant.txt if necessary

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
