# Lesson 1: Overview

![architecture.png](https://github.com/kevinwlu/iot/blob/master/lesson1/architecture.png)

* IoT architecture source: [IERC-European Research Cluster on the Internet of Things](http://www.internet-of-things-research.eu/pdf/IoT-From%20Research%20and%20Innovation%20to%20Market%20Deployment_IERC_Cluster_eBook_978-87-93102-95-8_P.pdf)
* [Open Systems Interconnecton (OSI) model](https://en.wikipedia.org/wiki/OSI_model)
* [Embedded system](https://en.wikipedia.org/wiki/Embedded_system)
* [Machine to machine](https://en.wikipedia.org/wiki/Machine_to_machine) (M2M) communication
* [IEEE International Network Generations Roadmap](https://futurenetworks.ieee.org/roadmap) (INGR)
* [Wide area network](https://en.wikipedia.org/wiki/Wide_area_network) (WAN)
* [Local area network](https://en.wikipedia.org/wiki/Local_area_network) (LAN)
  * [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi)
  * [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11)
  * [Li-Fi](https://en.wikipedia.org/wiki/Li-Fi)
* [Personal area network](https://en.wikipedia.org/wiki/Personal_area_network) (PAN)
  * [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth)
  * [Zigbee](https://en.wikipedia.org/wiki/Zigbee)
  * [6LoWPAN](https://en.wikipedia.org/wiki/6LoWPAN) (IPv6 over Low-Power Wireless Personal Area Network)
* [Near-field communication](https://en.wikipedia.org/wiki/Near-field_communication) (NFC)
* [Human-computer interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
  * [OpenBCI](https://en.wikipedia.org/wiki/OpenBCI)
* [Satellite internet access](https://en.wikipedia.org/wiki/Satellite_Internet_access)
  * [Kuiper Systems](https://en.wikipedia.org/wiki/Kuiper_Systems)
  * [OneWeb satellite constellation](https://en.wikipedia.org/wiki/OneWeb_satellite_constellation)
  * [Planet Labs](https://en.wikipedia.org/wiki/Planet_Labs)
  * [Starlink](https://en.wikipedia.org/wiki/Starlink)
* [Software-defined networking](https://en.wikipedia.org/wiki/Software-defined_networking) (SDN)
* [Network function virtualization](https://en.wikipedia.org/wiki/Network_function_virtualization) (NFV)
* [Network slicing](https://en.wikipedia.org/wiki/5G_network_slicing)
* [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)
* [As a service](https://en.wikipedia.org/wiki/As_a_service)
* [Orchestration](https://en.wikipedia.org/wiki/Orchestration_(computing))
* [Quality of service](https://en.wikipedia.org/wiki/Quality_of_service) (QoS)
* [Authentication, Authorization, and Accounting](https://en.wikipedia.org/wiki/AAA_(computer_security)) (AAA)
* [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) (CLI)
  * [Ping](https://en.wikipedia.org/wiki/Ping_(networking_utility))
  * [Localhost](https://en.wikipedia.org/wiki/Localhost)
* [Tunneling protocol](https://en.wikipedia.org/wiki/Tunneling_protocol)
  * [SSH](https://en.wikipedia.org/wiki/Secure_Shell)
  * [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (Elliptic Curve Digital Signature Algorithm)
  * [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing)

## Lab 1A: Raspberry Pi and Wi-Fi

* [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) only supports [SDHC](https://en.wikipedia.org/wiki/SD_card) (High Capacity up to 32 GB) cards with the FAT ([File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)) file system
* Any SD card larger than 32 GB is an SDXC card with the [exFAT](https://en.wikipedia.org/wiki/ExFAT)) file system that needs to be reformatted as FAT32 first
  * [Formatting an SXDC card](https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md)

### 1. On a laptop computer, download and open [Raspberry Pi Imager](https://www.raspberrypi.org/software/) 

* Insert an SD card to the laptop computer
* Click "CHOOSE OS" and select "Raspberry Pi OS (32-bit)" or "Erase (Format card as FAT32)"
* Click "CHOOSE SD CARD" and select the SD card
* Click "WRITE"
* Eject the SD card properly

### 2. Boot up a Raspberry Pi with the SD card for the first time

* Insert the SD card to the Raspberry Pi SD card slot
* Connect the Raspberry Pi with a display, keyboard, and mouse 
* Connect power to the Raspberry Pi

#### Alternatively, set up Raspberry Pi without a display, keyboard, and mouse

* Avram Piltch, [How to Set Up a Headless Raspberry Pi, Without Ever Attaching a Monitor](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html), June 25, 2020

### 3. Set up Raspberry Pi OS

* Set country, language, and timezone
* Select "Use English language" and "Use US keyboard" if applicable
* Change password (default: raspberry)
* Select if "this screen shows a black border around the desktop"
* Select wireless network and enter wireless network password
* Check and update software if necessary (this may involve a large download)
* Click "Restart" to reboot

### 4. Find a [MAC address](https://en.wikipedia.org/wiki/MAC_address) of the [media access control](https://en.wikipedia.org/wiki/Medium_access_control) with an [oranizationally unique identifier](https://en.wikipedia.org/wiki/Organizationally_unique_identifier) (OUI), and an [IP address](https://en.wikipedia.org/wiki/IP_address) of the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol)

* On [macOS](https://en.wikipedia.org/wiki/MacOS) or [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS), open a [terminal](https://en.wikipedia.org/wiki/Terminal_emulator) and enter
```sh
uname -a
ifconfig
ping localhost
```
* Alternatively on Raspberry Pi OS, point (not click) the curser to the Wi-Fi icon at the right of the menu bar to see and write down the IP address such as 192.168.1.204 excluding the CIDR ([Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)) notation of /24 suffix that indicates the number of bits of the prefix
* On [Windows](https://en.wikipedia.org/wiki/Windows_10), open [Command Promt](https://en.wikipedia.org/wiki/Cmd.exe), [PowerShell](https://en.wikipedia.org/wiki/PowerShell), or [Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal)
```sh
winver
ipconfig /all
ping localhost
```

## Lab 1B: Configuration

### 1. Click the Raspberry Pi icon at the left of the menu bar to open applications menu > Preferences > Raspberry Pi Configuration > System

* Change Hostname (default: raspberrypi)
* Disable "Auto login" 
* Enable "Network at Boot" to "Wait for network"
* Enable "[Splash Screen](https://en.wikipedia.org/wiki/Splash_screen)" (default)

### 2. Raspberry Pi Configuration > Display

* Disable "[Overscan](https://en.wikipedia.org/wiki/Overscan)" if the screen shows a black border around the desktop
* Disable "Pixel Doubling" (default)
* Enable "Screen Blanking" (default)

### 3. Raspberry Pi Configuration > Interfaces

* Enable Camera to use J3 Camera Serial Interface (CSI) 
* Enable SSH, VNC, SPI, I2C, Serial Port, 1-Wire, and Remote GPIO
* Disable Serial Console

### 4. Click OK and click Yes for "Would you like to reboot now?"

## Lab 1C: Startup Mailer
* The following steps that require the internet access are necessary only if the IP address of Raspberry Pi is unknown

### 1. Enable Google 2-Step Verification and generate a Google App 16-letter password

* My Account > Sign-in & security > Signing in to Google > 
* 2-Step Verification > TURN ON > Select a second verification step > Authenticator app (Default)
* App passwords > Select the app (Mail) and device (Raspberry Pi) > GENERATE

### 2. Click the [Terminal](https://www.raspberrypi.org/documentation/usage/terminal/) icon at the left of the menu bar

#### Clone the IoT repository on a Raspberry Pi
```sh
pi@raspberrypi:~ $ git clone https://github.com/kevinwlu/iot.git
```

#### Update the IoT repository on a Raspberry Pi afterwards
```sh
pi@raspberrypi:~ $ cd iot
pi@raspberrypi:~/iot $ git pull
```

#### Copy any file out of the IoT repository to edit
```sh
$ cp ~/iot/lesson1/startup_mailer.py .
```
* "~" represents the directory /home/pi
* "." represents the current directory
* ".." represents the parent directory
* Use a text editor such as the [GNU nano](https://en.wikipedia.org/wiki/GNU_nano)
```sh
$ nano startup_mailer.py
```
* Change RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD
* Replace HOSTNAME with the new Hostname in two instances
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

### 3. Check RECIPIENT_EMAIL for Hostname IP address

If not receiving an email from the Raspberry Pi, make sure startup_mailer.py is working
```sh
$ python3 ~/startup_mailer.py
```

### 4. Disconnect the monitor, keyboard, and mouse

## Lab 1D: [SSH](https://en.wikipedia.org/wiki/Secure_Shell) and [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing)

### 1. On a laptop, download [VNC Viewer](https://www.realvnc.com/download/viewer)

### 2. Open a Terminal on macOS/Linux or any of the following [terminal emulators](https://en.wikipedia.org/wiki/Terminal_emulator) on Windows
* [Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal)
* [Git Bash](https://gitforwindows.org/)
* [PuTTY](https://en.wikipedia.org/wiki/PuTTY)
### 3. Run an SSH client to log into Raspberry Pi
```sh
$ ssh pi@192.168.1.204
pi@raspberrypi:~ $ vncserver
```
### 4. Open VNC Viewer, and enter 192.168.1.204:1, username pi, and password

### 5. Click the Web Browser icon to launch [Chromium](https://en.wikipedia.org/wiki/Chromium_(web_browser))

### 6. Always shutdown Raspberry Pi properly from the applications menu or from the Terminal
```sh
$ sudo shutdown -h now
```
### 7. After the Raspberry Pi green LED blinks ten times, it's safe to pull the power
* The Raspberry Pi 4 uses the onboard [EEPROM](https://en.wikipedia.org/wiki/EEPROM) instead of bootcode.bin in the [boot folder](https://www.raspberrypi.org/documentation/configuration/boot_folder.md)
## Alternative 1: VNC Connect

* VNC Connect is included with the latest NOOBS for non-commercial use
* Sign up for a free [RealVNC](https://www.realvnc.com) account (need to be over 16) by an email address
* On the Raspberry Pi desktop, click the VNC Server icon at the right of the menu bar and sign in to enable cloud connectivity
* On a laptop, sign in to VNC Viewer

## Alternative 2: [Serveo](https://github.com/milio48/serveo) Port Forwarder

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
