# <a href="https://goo.gl/4aXo9L">Lesson 1</a>: Overview

## Lab A: NOOBS and Wi-Fi

### 1. Raspberry Pi only supports SDHC (High Capacity up to 32GB) cards with the FAT (File Allocation Table) file system

### 2. On a laptop, download the latest New Out-Of-Box Software (<a href="https://www.raspberrypi.org/downloads/noobs/">NOOBS</a>) zip file and extract the zip file to a folder

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

## Lab C: Startup Mailer - the following steps require the internet access

### 1. Enable Google 2-Step Verification and generate a Google App password

* My Account > Sign-in & security > Signing in to Google > 

* 2-Step Verification > TURN ON > Select a second verification step > Authenticator app (Default)

* App passwords > Select the app (Mail) and device (Raspberry Pi) > GENERATE

### 2. Click the Terminal icon at the left of the menu bar to open a Terminal and enter 

```sh
$ git clone https://github.com/kevinwlu/iot.git
$ cp ~/iot/lesson1/startup_mailer.py .
```
* "~" represents the directory /home/pi
* "." represents the current directory
```sh
$ nano startup_mailer.py
```
* Change RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD
* Replace HOSTNAME with the new Hostname
* Save the file by typing "control-x y enter"
```sh
$ sudo nano /etc/rc.local
```
* Add the following line with two-space indent above fi at the end as follows
```sh
  python3 /home/pi/startup_mailer.py
fi
```
* Save the file by typing "control-x y enter"
```sh
$ sudo reboot
```
### 3. Make /lib/systemd/system/rc-local.service executable if it's not
```sh
$ ls -l /lib/systemd/system/rc-local.service
$ sudo chmod +x /lib/systemd/system/rc-local.service
```
### 4. Check RECIPIENT_EMAIL for Hostname IP address

### 5. Disconnect the monitor, keyboard, and mouse

## Lab D: SSH and VNC

### 1. On a laptop, download VNC Viewer https://www.realvnc.com/download/viewer

### 2. Open a Terminal (or PuTTY) and enter
```sh
$ ssh pi@155.246.x.x
pi@raspberrypi:~ $ vncserver
```
### 3. Open VNC Viewer, and enter 155.246.x.x:1, username pi, and password

### 4. Click the Web Browser icon to launch Chromium

### 5. Always shutdown Raspberry Pi properly from the applications menu or from the Terminal
```sh
$ sudo shutdown -h now
```
### 6. Always unplug the power after the Raspberry Pi green LED blinks ten times

## Alternative 1: VNC Connect

* VNC Connect is included with the latest NOOBS for non-commercial use

* Sign up for a free RealVNC https://www.realvnc.com account (need to be over 16) by an email address

* On the Raspberry Pi desktop, click the VNC Server icon at the right of the menu bar and sign in to enable cloud connectivity

* On a laptop, sign in to VNC Viewer

## Alternative 2: Serveo Port Forwarder

* On a Raspberry Pi, copy two files
```sh
    pi@UNIQUE_NAME:~ $ cp ~/iot/lesson1/startup.cnf .
    pi@UNIQUE_NAME:~ $ cp ~/iot/lesson1/sshscript.sh .
```
* Edit sshscript.sh with a unique hostname
```sh
    pi@UNIQUE_NAME:~ $ sudo nano sshscript.sh
```
```sh
    #!/bin/bash   
    while :   
    do   
    ssh -R UNIQUE_NAME:22:localhost:22 serveo.net   
    sleep 10  
    done
```
```sh
    pi@UNIQUE_NAME:~ $ chmod +x sshscript.sh && sshscript.sh
```
* Edit /etc/rc.local
```sh
    $ sudo nano /etc/rc.local
```
```sh
    ...
    if grep -q "RunServeoSSHOnStartup=1" /home/pi/startup.cnf; then sudo /home/pi/sshscript.sh &  
    fi 
    exit 0
```
* On a laptop, run the following command
```sh
    $ ssh -J serveo.net pi@UNIQUE_NAME
```
