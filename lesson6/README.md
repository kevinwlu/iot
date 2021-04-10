# Lesson 6: Alternative Devices

* [Arduino](https://en.wikipedia.org/wiki/Arduino)
* [BeagleBoard](https://en.wikipedia.org/wiki/BeagleBoard)
* [ESP8266](https://en.wikipedia.org/wiki/ESP8266)
* [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set)
* [Node.js](https://en.wikipedia.org/wiki/Node.js)
* [Node-RED](https://en.wikipedia.org/wiki/Node-RED)
* [MEAN](https://en.wikipedia.org/wiki/MEAN_(solution_stack))
* [Mustache](https://en.wikipedia.org/wiki/Mustache_(template_system))
* [Handlebars.js](https://handlebarsjs.com/)
* [Pystache](https://github.com/defunkt/pystache)
* [OpenWrt](https://en.wikipedia.org/wiki/OpenWrt)
* [MATLAB Mobile](https://www.mathworks.com/products/matlab-mobile.html)

## Lab 6A: Node.js

### On Raspberry Pi via VNC Viewer, click the application menu on the left upper corner, select Programming to check whether Node-RED is installed

### If Node-RED is not installed, select Preferences > Recommended Software to install Node-RED

### Run and view Node.js server at http://127.0.0.1:8080 on Raspberry Pi via VNC viewer or directly at http://192.168.x.xxx:8080 on a laptop computer

### Reload the web page to see the server responses and press control-c (^C) to quit
```sh
$ node -h
$ node -v
$ cd ~/iot/lesson6
$ cat hello.js
$ node hello.js
Server running at http://127.0.0.1:8080/
response end call done
request end event fired
response end call done
request end event fired
^C
$ cat http.js
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
```

## Optional Lab 6C: Particle Cloud

[The Particle on Raspberry Pi project has been discontinued](https://docs.particle.io/raspberry-pi/)

* Uninstall Particle Agent and it dependencies on Raspberry Pi 4B if 
    * Error claiming Raspberry Pi 4B to the Particle account
    * Raspberry Pi 4B green LED is on constantly

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
