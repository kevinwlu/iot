# <a href="https://goo.gl/4aXo9L">Lesson 1</a>: Overview

## Lab A: NOOBS and Wi-Fi

### 1. Raspberry Pi only supports SDHC (High Capacity up to 32GB) cards with the FAT (File Allocation Table) file system

### 2. On a laptop, download the latest New Out-Of-Box Software (NOOBS) zip file and extract the zip file to a folder

* Insert a new or reformatted SD card, go to the folder, select all items, then drag and drop them to the SD card

* Eject the SD card properly, and insert it to Raspberry Pi SD card slot

### 3. Install NOOBS first at Burchard 123 on the Stevens Wi-Fi network by connecting Raspberry Pi to a monitor, keyboard, and mouse, then to power

* Click "Wifi network (w)," select "Stevens," enter Stevens Username and Password — once connected, more operating systems become available

* Select "Raspbian Full [RECOMMENDED]" and "English (US) Language and Keyboard"

* Click "Install (i)" and OK — installable without the internet access

* Click OK after "OS(es) Installed Successfully" to reboot

### 4. After reboot, change Password (default: raspberry) and skip both Wi-Fi and update

## Lab B: Configuration

### 1. Click the Raspberry Pi icon at the left of the menu bar to open applications menu > Preferences > Raspberry Pi Configuration > System

* Change Hostname (default: raspberrypi)

* Disable "Auto login" 

* Enable "Network at Boot" to "Wait for network"

* Disable overscan if there is a black border on the display

### 2. Raspberry Pi Configuration > Interfaces

* Enable SSH, VNC, SPI, I2C, Serial Port, 1-Wire, and Remote GPIO

* Disable Serial Console

### 3. Click OK

### 4. Click Yes for "Would you like to reboot now?"

## Lab C: Startup Mailer

### 1. The following steps require the internet access

### 2. Click the Terminal icon at the left of the menu bar to open a Terminal and enter 

$ git clone https://github.com/kevinwlu/iot.git

$ cp ~/iot/lesson1/startup_mailer.py .

* "~" represents the directory /home/pi

$ nano startup_mailer.py

### 3. Change RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD

* My Account > Sign-in & security > Signing in to Google > 

* 2-Step Verification > TURN ON > Select a second verification step > Authenticator app (Default)

* App passwords > Select the app (Mail) and device (Raspberry Pi) > GENERATE

### 4. Replace HOSTNAME with the new Hostname

### 5. Save the file by typing "control-x y enter" and enter

$ sudo nano /etc/rc.local

### 6. Add the following line with two-space indent above fi at the end as follows

&nbsp;  python3 /home/pi/startup_mailer.py

fi

### 7. Save the file by typing "control-x y enter" and enter

$ sudo reboot

### 8. Disconnect the monitor, keyboard, and mouse

### 9. Check RECIPIENT_EMAIL for Hostname IP address

## Lab D: SSH and VNC

### 1. On a laptop, download VNC Viewer https://www.realvnc.com/download/viewer

### 2. Open a GNU Bash Terminal (or PuTTY) and enter

$ ssh pi@155.246.x.x

pi@raspberrypi:~ $ vncserver

### 3. Open VNC Viewer, and enter 155.246.x.x:1, username pi, and password

### 4. Click the Web Browser icon to launch Chromium

### 5. Always shutdown Raspberry Pi properly from the applications menu or from the Terminal

$ sudo shutdown -h now

### 6. Always unplug the power after the Raspberry Pi green LED blinks ten times
