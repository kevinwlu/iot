# Lesson 1: Overview

> [Kevin Ashton](https://en.wikipedia.org/wiki/Kevin_Ashton), *[How to Fly a Horse](https://en.wikipedia.org/wiki/How_to_Fly_a_Horse): The Secret History of Creation, Invention, and Discovery.* It's about [the way innovation really happens](https://www.newsweek.com/2015/03/06/meet-kevin-ashton-father-internet-things-308763.html), which is less by magic and genius than by a lot of small steps and bits of luck.

![architecture.png](https://github.com/kevinwlu/iot/blob/master/lesson1/architecture.png)

* IoT architecture source: [IERC-European Research Cluster on the Internet of Things](http://www.internet-of-things-research.eu/pdf/IoT-From%20Research%20and%20Innovation%20to%20Market%20Deployment_IERC_Cluster_eBook_978-87-93102-95-8_P.pdf)
* [Open Systems Interconnecton (OSI) model](https://en.wikipedia.org/wiki/OSI_model)
* [Embedded system](https://en.wikipedia.org/wiki/Embedded_system)
* [Machine to machine](https://en.wikipedia.org/wiki/Machine_to_machine) (M2M) communication
* [Network packet](https://en.wikipedia.org/wiki/Network_packet)
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
* [Cobot](https://en.wikipedia.org/wiki/Cobot) or collaborative robot
* [Human-computer interaction](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)
  * [OpenBCI](https://en.wikipedia.org/wiki/OpenBCI)
* [BRAIN Initiative](https://en.wikipedia.org/wiki/BRAIN_Initiative) (Brain Research Through Advancing Innovative Neurotechnologies)
  * [BRAIN Initiative](https://www.braininitiative.org/)
  * [Brain Initiative](https://braininitiative.nih.gov/) | NIH (National Institutes of Health) 
  * [IEEE Brain Initiative](https://brain.ieee.org/)
* [Satellite internet access](https://en.wikipedia.org/wiki/Satellite_Internet_access)
  * [Kuiper Systems](https://en.wikipedia.org/wiki/Kuiper_Systems)
  * [OneWeb satellite constellation](https://en.wikipedia.org/wiki/OneWeb_satellite_constellation)
  * [Planet Labs](https://en.wikipedia.org/wiki/Planet_Labs)
  * [Starlink](https://en.wikipedia.org/wiki/Starlink)
* [Software-defined networking](https://en.wikipedia.org/wiki/Software-defined_networking) (SDN)
* [Network function virtualization](https://en.wikipedia.org/wiki/Network_function_virtualization) (NFV)
* [Network slicing](https://en.wikipedia.org/wiki/5G_network_slicing)
* [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing)
  * [DevOps](https://en.wikipedia.org/wiki/DevOps)
  * Google Cloud [DevOps Research and Assessment](https://cloud.google.com/devops) (DORA)
* [Edge computing](https://en.wikipedia.org/wiki/Edge_computing)
* [As a service](https://en.wikipedia.org/wiki/As_a_service)
* [Orchestration](https://en.wikipedia.org/wiki/Orchestration_(computing))
* [Quality of service](https://en.wikipedia.org/wiki/Quality_of_service) (QoS)
* [Authentication, Authorization, and Accounting](https://en.wikipedia.org/wiki/AAA_(computer_security)) (AAA)
* [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) (CLI)
  * [Termina emulator](https://en.wikipedia.org/wiki/Terminal_emulator)
  * [sudo](https://en.wikipedia.org/wiki/Sudo)
  * [Ping](https://en.wikipedia.org/wiki/Ping_(networking_utility))
  * [scrot](https://en.wikipedia.org/wiki/Scrot) vs. screencapture on macOS
  * [Localhost](https://en.wikipedia.org/wiki/Localhost)
  * [Keyboard shortcut](https://en.wikipedia.org/wiki/Keyboard_shortcut)
  * [Control-D](https://en.wikipedia.org/wiki/End-of-Transmission_character)
* [Tunneling protocol](https://en.wikipedia.org/wiki/Tunneling_protocol)
* [SSH](https://en.wikipedia.org/wiki/Secure_Shell)
  * [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) (Rivest–Shamir–Adleman)
  * [DSA](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm) (Digital Signature Algorithm)
  * [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (Elliptic Curve Digital Signature Algorithm)
  * [EdDSA](https://en.wikipedia.org/wiki/EdDSA) (Edwards-curve Digital Signature Algorithm) such as Ed25519
* [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing)

## Lab 1A: Raspberry Pi Setup

* [Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi) supports [SDHC](https://en.wikipedia.org/wiki/SD_card) (High Capacity up to 32 GB) cards with the FAT ([File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)) file system
* [Examples of 32 GB microSD cards](https://www.tomshardware.com/best-picks/raspberry-pi-microsd-cards)
* Any SD card larger than 32 GB is likely an SDXC card with the [exFAT](https://en.wikipedia.org/wiki/ExFAT) file system that won't boot
* [Raspberry Pi Imager](https://www.raspberrypi.org/software/) can erase and format any SD card as FAT32
* Raspberry Pi OS [releases](http://downloads.raspberrypi.org/NOOBS/images/) since 2013-06-27
  * Formerly [NOOBS](https://github.com/raspberrypi/noobs) (New Out-Of-Box Software)
* Raspberry Pi OS [release notes](https://downloads.raspberrypi.org/raspios_armhf/release_notes.txt) since 2013-09-10

### 1. On a laptop computer, download and open [Raspberry Pi Imager](https://www.raspberrypi.org/software/)

* Insert an SD card to the laptop computer
* Click "CHOOSE OS" and select "Raspberry Pi OS (32-bit)" or "Erase (Format card as FAT32)"
* Click "CHOOSE STORAGE" and select the SD card
* Click "WRITE" and "YES"
* Upon "Write Successful," click "CONTINUE" to eject the SD card properly

### 2. Boot up a Raspberry Pi with the SD card for the first time

* Insert the SD card to the Raspberry Pi SD card slot
* Connect the Raspberry Pi with a display, keyboard, and mouse 
* Connect power to the Raspberry Pi

#### Alternatively, set up Raspberry Pi without a display, keyboard, and mouse

* Avram Piltch, [How to Set Up a Headless Raspberry Pi, Without Ever Attaching a Monitor](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html), June 25, 2020

### 3. Set up Raspberry Pi OS

* Welcome to Raspberry Pi > Next 
* Set country, language, and timezone and select "Use English language" and "Use US keyboard" if applicable > Next
* Change [password](https://en.wikipedia.org/wiki/Password) (default: raspberry) > Next
* Set up screen: click the box if "the taskbar does not fit onto the screen" > Next
* Select Wi-Fi network > Next
* Enter Wi-Fi password > Next
* Update software > Next > System is up to date > OK
* Setup complete > Restart

### 4. Raspberry Pi desktop preferences

* On Raspberry Pi desktop > Right click > Desktop Preferences > Appearance Settings
* Desktop (Layout, Picture, Color, Text Color, Documents, Wastebasket, Mounted Disks)
* Menu Bar (Size, Position, Color, Text Color)
* System (Font, Highlight Color, Highlight Text Color, Mouse Cursor)
* Defaults (For large, medium, or small screens)

### 5. Find a [MAC address](https://en.wikipedia.org/wiki/MAC_address) of the [media access control](https://en.wikipedia.org/wiki/Medium_access_control) with an [oranizationally unique identifier](https://en.wikipedia.org/wiki/Organizationally_unique_identifier) (OUI), and an [IP address](https://en.wikipedia.org/wiki/IP_address) of the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol)

* On [macOS](https://en.wikipedia.org/wiki/MacOS) or [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS), open a [GNOME Terminal](https://en.wikipedia.org/wiki/GNOME_Terminal) and enter
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

## Lab 1B: Raspberry Pi Configuration

### 1. Click the Raspberry Pi icon at the left of the menu bar to open applications menu > Preferences > Raspberry Pi Configuration > System

* Change [Hostname](https://en.wikipedia.org/wiki/Hostname) (default: raspberrypi)
* [Boot](https://en.wikipedia.org/wiki/Booting) (default: To Desktop)
* Auto [login](https://en.wikipedia.org/wiki/Login) (default: login as user 'pi') > Disabled (otherwise anyone can power up and auto login)
* Network at Boot (default: Do not wait) > Wait for network (to run startup_mailier.py)
* [Splash Screen](https://en.wikipedia.org/wiki/Splash_screen) (default: Enable)
* Power LED (default: Activity)

### 2. Raspberry Pi Configuration > Display

* [Overscan](https://en.wikipedia.org/wiki/Overscan) (default: Disable) > Enable if the screen shows a black border around the desktop
* Pixel Doubling (default: Disable)
* Screen Blanking (default: Enable)
* Headless Resolution: 640x480, 720x480, 800x600, 1024x768, 1280x720, 1280x1024, 1600x1200, 1920x1080

### 3. Raspberry Pi Configuration > Interfaces

* Camera > Enable the [Camera Serial Interface](https://en.wikipedia.org/wiki/Camera_Serial_Interface) (CSI) marked as J3 to use a [Raspberry Pi Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
  * [Raspberry Pi Camera Module 2](https://www.raspberrypi.com/products/camera-module-v2/)
  * In contrast, the [Display Serial Interface](https://en.wikipedia.org/wiki/Display_Serial_Interface) (DSI) marked as J4 is [plug and play](https://en.wikipedia.org/wiki/Plug_and_play) to use a [Raspberry Pi Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/)
* [SSH](https://en.wikipedia.org/wiki/Secure_Shell) (defaut: Disable) > Enable
* [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing) (defaut: Disable) > Enable
* [SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) (defaut: Disable) > Enable
* [I2C](https://en.wikipedia.org/wiki/I%C2%B2C) (defaut: Disable) > Enable
* [Serial](https://en.wikipedia.org/wiki/Serial_communication) Port (defaut: Disable) > Enable
* [Serial Console](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable) (default: Enable) > Disable
  * 2018-06-27: Serial port and serial console can now be switched separately in Raspberry Pi Configuration
* [1-Wire](https://en.wikipedia.org/wiki/1-Wire) (defaut: Disable) > Enable
* Remote [GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output) (defaut: Disable) > Enable

### 4. Raspberry Pi Configuration > Performance

* [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) Memory (default: 64)
* Overlay File System (default: Overlay > Disabled, Boot Partition > Read-write)
* Fan (dafault: Diable)
* Fan GPIO (default: 14)
* Fan Temperature (default: 80)

### 5. Raspberry Pi Configuration > Localization

* Locale > Language, Country, Character Set > OK
* Timezone > Area, Location > OK
* Keyboard > Model, Layout, Variant > OK
* Wi-Fi Country > Country > OK

### 6. Click OK and click Yes for "Would you like to reboot now?"

### 7. Raspberry Pi requires proper shutdown

* Raspberry Pi applications menu > Logout > Shutdown options: Shutdown, Reboot, Logout > Shutdown
* After the Raspberry Pi green LED blinks ten times, it's safe to unplug the power
* WARNING: Unplugging the power without proper shutdown may [corrupt](https://en.wikipedia.org/wiki/Data_corruption) the SD card

## Lab 1C: Startup Mailer
* The following steps require the internet access
* /etc/rc.local does not work with Raspberry Pi OS 11 (Bullseye)
* The starup mailer is useful when the IP address of Raspberry Pi is dynamic on the public or enterprise Wi-Fi network
* The IP address is usually static on the personal Wi-Fi network or cellular personal hotspot

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
* Test startup_mailer.py
* Edit /etc/rc.local
```sh
$ python3 ~/startup_mailer.py
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

If not receiving an email from the Raspberry Pi after reboot, create /lib/systemd/system/[startup.service](/startup.service)
```sh
$ sudo nano /lib/systemd/system/startup.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable startup.service
$ sudo reboot
```

### 4. Disconnect the monitor, keyboard, and mouse

## Lab 1D: [SSH](https://en.wikipedia.org/wiki/Secure_Shell) and [VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing)

### 1. On a laptop, download [VNC Viewer](https://www.realvnc.com/download/viewer)

### 2. Open a Terminal on macOS/Linux or any of the following [terminal emulators](https://en.wikipedia.org/wiki/Terminal_emulator) on Windows
* [Windows Subsystem for Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) (WSL) Linux Terminal (Ubuntu by default)
  * Installing [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) requires Windows 11 or a higher version (or build) of Windows 10
  * Join the [Windows Insiders Program](https://insider.windows.com/en-us/getting-started) if necessary
* [Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal)
* [Git for Windows](https://gitforwindows.org/)
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
### 7. After the Raspberry Pi green LED blinks ten times, it's safe to unplug the power
* The Raspberry Pi 4 uses the onboard [EEPROM](https://en.wikipedia.org/wiki/EEPROM) instead of bootcode.bin in the [boot folder](https://www.raspberrypi.org/documentation/configuration/boot_folder.md)

## Alternative 1: VNC Connect

* VNC Connect is included with Raspberry Pi OS for non-commercial use
* Sign up for a free [RealVNC](https://www.realvnc.com) account (need to be over 16) by an email address
* On the Raspberry Pi desktop, click the VNC Server icon at the right of the menu bar and sign in to enable cloud connectivity
* On a laptop, sign in to VNC Viewer

## Alternative 2: Ngrok

* Sign up [ngrok](https://ngrok.com/)
* Download ngrok to Raspberry Pi
* Copy the Authtoken to authenticate the ngrok downloaded
* Authtoken is saved to configuration file: /home/pi/.ngrok2/ngrok.yml
```sh
$ sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
$ sudo unzip ngrok-stable-linux-arm.zip
$ ./ngrok authtoken <the Authtoken>
Authtoken saved to configuration file: /home/pi/.ngrok2/ngrok.yml
$ ./ngrok tcp 22
```
* Copy the forwarding URL 6.tcp.ngrok.io and the port number
* On another computer, ssh Raspberry Pi
```sh
ssh pi@6.tcp.ngrok.io -p <the port number>
```
* On Raspberry Pi
  * Ctrl+U to update ngrok if available
  * Ctrl+C to quit ngrok

## Alternative 3: [Serveo](https://github.com/milio48/serveo) Port Forwarder

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
