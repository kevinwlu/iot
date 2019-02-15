# <a href="https://goo.gl/4aXo9L">Lesson 1</a>: Overview

## Lab A: NOOBS and Wi-Fi

### 1. Download the New Out Of Box Software (NOOBS) in ZIP at https://www.raspberrypi.org/downloads/noobs

### 2. Extract the NOOBS ZIP file to a folder and select all items in the folder

### 3. Copy all items to a 32GB micro Secure Digital High Capacity (SDHC) memory card

### 4. Insert the microSDHC memory card to a Raspberry Pi

### 5. Connect the Raspberry Pi to a HDMI monitor, and USB keyboard and mouse

### 6. Connect the Raspberry Pi to a micro-USB 5V 2.5A power supply

### 7. Click "Wi-Fi network," select network, and enter username and password

### 8. Select "Raspbian" and "English (US) Language and Keyboard," click "Install" and "OK"

### 9. Click "OK" to reboot after "OS(es) Installed Successfully"

### 10. Click "Next" to set country and change password

### 11. Skip Wi-Fi Network and Updates

### 12. Reboot again

## Lab B: Configuration

### 1. Pull down the Raspberry Pi menu, and select "Preferences" and "Raspberry Pi Configuration"

### 2. Change Hostname, disable "Auto Login," and enable "Wait for network" under the "System" tab

### 3. Enable SSH/VNC/SPI/I2C/Serial Port/1-Wire, and disable Serial Console under the "Interfaces" tab

### 4. Click "OK" and reboot

## Lab C: Startup Mailer

### 1. Open a command-line interface (CLI) Terminal

### 2. Clone IoT repository from GitHub

git clone https://github.com/kevinwlu/iot.git

### 3. Copy startup_mailer.py to the current directory "."

cp ~/iot/lesson1/startup_mailer.py .

### 4. Open a Chromium browser and go to https://myaccount.google.com

### 5. Click "Sign-in & security" and turn on 2-Step Verification

### 6. Select a second verification step with "Authenticator app"

### 7. Generate a 16-digit "App password" with the app as "Mail" and device as "Raspberry Pi" 

### 8. Edit startup_mailer.py by changing RECIPIENT_EMAIL, GMAIL_USERNAME, GOOGLE_APP_PASSWORD, and HOSTNAME

nano startup_mailer.py

### 9. Edit /etc/rc.local as in startup_mailer.txt

sudo nano /etc/rc.local

### 10. Set up Wi-Fi as in wpa_supplicant.txt if necessary

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
