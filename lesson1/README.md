# <a href="https://goo.gl/4aXo9L">Lesson 1</a>: Overview

## Lab A: NOOBS and Wi-Fi

### * Raspberry Pi only supports SDHC (High Capacity up to 32GB) cards with the FAT (File Allocation Table) file system

### * On a laptop, download the latest New Out-Of-Box Software (NOOBS) zip file and extract the zip file to a folder

#### * Insert a new or reformatted SD card, go to the folder, select all items, then drag and drop them to the SD card

#### * Eject the SD card properly, and insert it to Raspberry Pi SD card slot

### * Install NOOBS first at Burchard 123 on the Stevens Wi-Fi network by connecting Raspberry Pi to a monitor, keyboard, and mouse, then to power

#### * Click "Wifi network (w)," select "Stevens," enter Stevens Username and Password — once connected, more operating systems become available

#### * Select "Raspbian Full [RECOMMENDED]" and "English (US) Language and Keyboard"

#### * Click "Install (i)" and OK — installable without the internet access

#### * Click OK after "OS(es) Installed Successfully" to reboot

### * After reboot, change Password (default: raspberry) and skip Wi-Fi and update

## Lab B: Configuration

### * Click the Raspberry Pi icon at the left of the menu bar to open applications menu > Preferences > Raspberry Pi Configuration > System

#### * Change Hostname (default: raspberrypi)

#### * Disable "Auto login" 

#### * Enable "Network at Boot" to "Wait for network"

#### * Disable underscan if display has a black border

### * Raspberry Pi Configuration > Interfaces

#### * Enable SSH, VNC, SPI, I2C, Serial, and 1-Wire

### * Click OK

### * Click Yes for "Would you like to reboot now?"

## Lab C: Startup Mailer

### * The following steps require the internet access

### * Click the Terminal icon at the left of the menu bar to open a Terminal and enter 

$ git clone https://github.com/kevinwlu/iot.git

$ cp ~/iot/lesson1/startup_mailer.py .

#### * "~" represents the directory /home/pi

$ nano startup_mailer.py

### * Change RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD

#### * My Account > Sign-in & security > Signing in to Google > 

##### * 2-Step Verification > TURN ON > Select a second verification step > Authenticator app (Default)

##### * App passwords > Select the app (Mail) and device (Raspberry Pi) > GENERATE

### * Replace HOSTNAME with the new Hostname

### * Save the file by typing "control-x y enter" and enter

$ sudo nano /etc/rc.local

### * Add the following line above fi at the end as follows

python3 /home/pi/startup_mailer.py

fi

### * Save the file by typing "control-x y enter" and enter

$ sudo reboot

### * Disconnect the monitor, keyboard, and mouse

### * Check RECIPIENT_EMAIL for Hostname IP address

## Lab D: SSH and VNC

### * On a laptop, download VNC Viewer https://www.realvnc.com/download/viewer

### * Open a GNU Bash Terminal (or PuTTY) and enter

$ ssh pi@155.246.x.x

pi@raspberrypi:~ $ vncserver

### * Open VNC Viewer, and enter 155.246.x.x:1, username pi, and password

### * Click the Web Browser icon to launch Chromium

### * Always shutdown Raspberry Pi properly from the applications menu or from the Terminal

$ sudo shutdown -h now

### * Always unplug the power after the Raspberry Pi green LED blinks ten times
