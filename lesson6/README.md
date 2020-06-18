# Lesson 6: Alternative Devices

## Lab 6A: Particle Cloud

[The Particle on Raspberry Pi project has been discontinued](https://docs.particle.io/datasheets/discontinued/raspberry-pi/)

### Sign up and log in Particle at https://www.particle.io

### Install the Particle-Agent on Raspberry Pi, log in the Particle account, and claim Raspberry Pi to the Particle account
```sh
$ bash <( curl -sL https://particle.io/install-pi )
```
### If the Raspberry Pi hostname has changed, run particle-agent again
```sh
sudo particle-agent setup
```
### Download, install, and open Particle Mobile App on a smartphone

### Log in Particle account and select Raspberry Pi

### Tinker > D7 > digitalWrite() > HIGH or LOW to toggle the green activity LED

### Alternately, install [Particle CLI](https://docs.particle.io/tutorials/developer-tools/cli/) on a laptop (not recommended for Raspberry Pi since it disables the color in Bash)

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

## Lab 6B: Node.js

### Run Node.js server at http://127.0.0.1:8080 on Raspberry Pi
```sh
$ node -h
$ node -v
$ cd ~/iot/lesson6
$ node hello.js
$ node http.js
```
