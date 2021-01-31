# Lesson 6: Alternative Devices

* [Arduino](https://en.wikipedia.org/wiki/Arduino)
* [BeagleBoard](https://en.wikipedia.org/wiki/BeagleBoard)
* [RSP8266](https://en.wikipedia.org/wiki/ESP8266)
* [Hayes command set](https://en.wikipedia.org/wiki/Hayes_command_set)
* [Node.js](https://en.wikipedia.org/wiki/Node.js)
* [Node-RED](https://en.wikipedia.org/wiki/Node-RED)
* [MATLAB Mobile](https://www.mathworks.com/products/matlab-mobile.html)
* [MEAN](https://en.wikipedia.org/wiki/MEAN_(solution_stack))
* [OpenWrt](https://en.wikipedia.org/wiki/OpenWrt)

## Lab 6A: Node.js

### Run and view Node.js server at http://127.0.0.1:8080 on Raspberry Pi via VNC viewer or directly at http://192.168.x.xxx:8080 on a laptop computer
```sh
$ node -h
$ node -v
$ cd ~/iot/lesson6
$ node hello.js
$ node http.js
```

## Lab 6B: Particle Cloud

[The Particle on Raspberry Pi project has been discontinued](https://docs.particle.io/raspberry-pi/)

### Sign up and log in Particle at https://www.particle.io

### Install the Particle-Agent on Raspberry Pi, log in the Particle account, and claim Raspberry Pi to the Particle account
```sh
$ bash <( curl -sL https://particle.io/install-pi )
```
### If the Raspberry Pi hostname has changed, run particle-agent again
```sh
$ sudo particle-agent setup
```
### Download, install, and open Particle Mobile App on a smartphone

### Log in Particle account and select Raspberry Pi

### Tinker > D7 > digitalWrite() > HIGH or LOW to toggle the green activity LED

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
