# Lesson 6: Alternative Devices

* [Embedded system](https://en.wikipedia.org/wiki/Embedded_system)
* [Microcontroller](https://en.wikipedia.org/wiki/Microcontroller)
* [Nvidia Jetson](https://en.wikipedia.org/wiki/Nvidia_Jetson)
* [BeagleBoard](https://en.wikipedia.org/wiki/BeagleBoard)
* [DragonBoard 410c](https://developer.qualcomm.com/hardware/dragonboard-410c)
* [Pine64](https://en.wikipedia.org/wiki/Pine64)
  * [Armbian](https://en.wikipedia.org/wiki/Armbian)
* [Arduino](https://en.wikipedia.org/wiki/Arduino)
  * [List of Arduino boards and compatible systems](https://en.wikipedia.org/wiki/List_of_Arduino_boards_and_compatible_systems)
  * [SoftwareSerial Library](https://www.arduino.cc/en/Reference/softwareSerial)
  * [OpenWrt](https://en.wikipedia.org/wiki/OpenWrt)
  * [Seeeduino XIAO](https://wiki.seeedstudio.com/Seeeduino-XIAO/) by [Seeed](https://www.seeed.cc/) 
  * [TinyDuino](https://tinycircuits.com/products/tinyduino-processor-board) by [TinyCircuits](https://tinycircuits.com/)
* [STM32](https://en.wikipedia.org/wiki/STM32)
  * [Nucleo-64](https://www.st.com/en/evaluation-tools/nucleo-f072rb.html)
  * [Mbed](https://en.wikipedia.org/wiki/Mbed)
  * [ARMmbed/mbed-os-example-blinky](https://github.com/ARMmbed/mbed-os-example-blinky)
* [Particle](https://www.particle.io/)
* [Redbear Duo](https://github.com/redbear/Duo)
* [Tessel](https://tessel.github.io/t2-start/)
* [ESP8266](https://en.wikipedia.org/wiki/ESP8266)
  * [ESP-01](https://jayconsystems.com/blog/getting-started-with-the-esp8266-esp-01)
  * [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set) or AT command set
  * [Zerynth](https://en.wikipedia.org/wiki/Zerynth)
* [ESP32](https://en.wikipedia.org/wiki/ESP32)
  * [Obsidian Boa](https://github.com/gregdavill/obsidian-boa)
* [AT&T IoT Starter Kit](https://github.com/att-iotstarterkits/sk2-Users-Guide)
  * [OpenEmbedded](https://en.wikipedia.org/wiki/OpenEmbedded)
  * [Yocto](https://en.wikipedia.org/wiki/Yocto_Project)
  * [M18Qx IoT Monitor](https://github.com/Avnet/M18QxIotMonitor)
  * [Anjay](https://github.com/AVSystem/Anjay)
  * [Eclipse Leshan](https://github.com/eclipse/leshan)
* [CoAP](https://en.wikipedia.org/wiki/Constrained_Application_Protocol) (Constrained Application Protocol)
  * [txThings](https://github.com/mwasilak/txThings)
  * [aiocoap](https://github.com/chrysn/aiocoap)
  * [CoAPthon3](https://github.com/Tanganelli/CoAPthon3)
* [u-blox EVK-R410M-02B](https://www.u-blox.com/en/product/evk-r4)
  * [m-center](https://www.u-blox.com/en/product/m-center)
* [Narrowband IoT](https://en.wikipedia.org/wiki/Narrowband_IoT) (NB-IoT)
* [LTE-M](https://en.wikipedia.org/wiki/LTE-M) Machine Type Communication
* [Global Positioning System](https://en.wikipedia.org/wiki/Global_Positioning_System) (GPS)
* [Hirose U.FL](https://en.wikipedia.org/wiki/Hirose_U.FL) connectors
* [Lithium-ion polymer (LiPo) battery](https://en.wikipedia.org/wiki/Lithium_polymer_battery)
* [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) (AES)
* [KASUMI](https://en.wikipedia.org/wiki/KASUMI) block cipher
* [Zuc stream cipher](https://en.wikipedia.org/wiki/Zuc_stream_cipher)
* [HarmonyOS](https://en.wikipedia.org/wiki/HarmonyOS)
* [Node.js](https://en.wikipedia.org/wiki/Node.js)
  * [npm](https://en.wikipedia.org/wiki/Npm_(software)) (Node Package Manager)
  * [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager)
  * [Firebase Quickstarts for Node.js](https://github.com/firebase/quickstart-nodejs)
  * [Build a simple CRUD Node.js app with CockroachDB and the node-postgres driver](https://www.cockroachlabs.com/docs/stable/build-a-nodejs-app-with-cockroachdb.html)
* [Node-RED](https://en.wikipedia.org/wiki/Node-RED)
  * [Low-code development platofrm](https://en.wikipedia.org/wiki/Low-code_development_platform) (LCDP)
* [OpenJS Foundation](https://en.wikipedia.org/wiki/OpenJS_Foundation#JS_Foundation)
* [MEAN](https://en.wikipedia.org/wiki/MEAN_(solution_stack)): [MongoDB](https://en.wikipedia.org/wiki/MongoDB), [Express.js](https://en.wikipedia.org/wiki/Express.js), [AngularJS](https://en.wikipedia.org/wiki/AngularJS), and Node.js
* [Mustache](https://en.wikipedia.org/wiki/Mustache_(template_system))
* [Handlebars.js](https://handlebarsjs.com/)
* [Pystache](https://github.com/defunkt/pystache)
* [MATLAB](https://en.wikipedia.org/wiki/MATLAB) (Matrix Laboratory)
* [MATLAB Mobile](https://www.mathworks.com/products/matlab-mobile.html)
* [Vysor](https://github.com/koush/vysor.io)

## Lab 6A: Node.js

### [Node.js Downloads](https://nodejs.org/en/download/) include latest Long Term Support (LTS) version and npm
* Pre-built installer and binary for Windows with an option to install (or upgrade) the necessary tools such as Chocalatey, Python, and Visual Studio
  * WARNING: Upgrading Python resets pip list with only pip and setuptools, requiring package reinstallation
* Pre-built installer and binary for macOS (/usr/local/bin)
* Linux binaries for x64 and ARM
```sh
$ node -v
$ npm -v
$ node -h
$ cd ~/iot/lesson6
$ node hello-world.js
$ node hello.js
Server running at http://127.0.0.1:8080/
response end call done
request end event fired
response end call done
request end event fired
^C
$ node http.js
0

1
2
^C
$
```
### On Raspberry Pi via VNC Viewer, click the application menu on the left upper corner, select Programming to check whether Node-RED is installed
* If Node-RED is not installed, select Preferences > Recommended Software to install Node-RED
* Alternative [installation](https://nodered.org/docs/getting-started/raspberrypi) as follows
```sh
$ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
* Run and view Node.js server at http://127.0.0.1:8080 on Raspberry Pi via VNC viewer or directly on a laptop computer at the Raspberry Pi IP address such as http://192.168.1.204:8080
* Reload the web page to see the server responses and press control-c (^C) to quit
```sh
$ node -v
$ npm -v
$ node -h
$ cd ~/iot/lesson6
$ node hello.js
Server running at http://127.0.0.1:8080/
response end call done
request end event fired
response end call done
request end event fired
^C
$ node http.js
0

1
2
^C
$
```
## Lab 6B: Pystache

### Install Pystache and run example code
```
$ sudo pip3 install pystache
$ cd ~/iot/lesson6
$ cat say_hello.mustache
$ cat say_hello.py
$ python3 say_hello.py
Hi Alexa!
Hello, World!

['Hey ', _SectionNode(key='who', index_begin=12, index_end=18, parsed=[_EscapeNode(key='.'), '!'])]
Hey Google!
Hey Siri!
$
```

## Optional Lab 6C: Particle Cloud

* [The Particle on Raspberry Pi project has been discontinued](https://docs.particle.io/raspberry-pi/)
* Raspberry Pi 4B is not supported
  * Error claiming Raspberry Pi 4B to the Particle account
  * Raspberry Pi 4B green LED is on constantly
  * Uninstall Particle Agent and its dependencies on Raspberry Pi 4B

### Sign up and log in Particle at https://www.particle.io

### Install the [Particle Agent](https://prerelease-docs.particle.io/reference/discontinued/particle-agent/) on Raspberry Pi, log in the Particle account, and claim Raspberry Pi to the Particle account
```sh
$ bash <( curl -sL https://particle.io/install-pi )
```
### If the Raspberry Pi hostname has changed, unclaim it on [Particle Console](https://console.particle.io/devices), and run particle-agent again
```sh
$ sudo particle-agent setup
```
### Download, install, and open Particle Mobile App on a smartphone

### Log in Particle account and select Raspberry Pi

### Tinker > D7 > digitalWrite() > HIGH or LOW to toggle the green activity LED

### To remove the [Particle Agent](https://prerelease-docs.particle.io/reference/discontinued/particle-agent/) and its dependencies
```sh
$ sudo apt remove particle-agent
$ sudo apt autoremove
$ sudo rm -rf /var/lib/particle
```

### Alternately, install [Particle CLI](https://docs.particle.io/tutorials/developer-tools/cli/) on a laptop (not recommended for Raspberry Pi since it disables the Bash color prompt)

#### Windows

* [Windows CLI installer](https://binaries.particle.io/cli/installer/windows/ParticleCLISetup.exe)

#### macOS or Linux

```sh
$ bash <( curl -sL https://particle.io/install-cli )
$ particle login
$ particle call <device_name> digitalwrite D7=HIGH
$ particle call <device_name> digitalwrite D7=LOW
$ particle logout
```
