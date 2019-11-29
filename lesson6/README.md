# <a href="https://goo.gl/KDtocJ">Lesson 6</a>: Alternative Devices

## Lab A: Particle Cloud

https://docs.particle.io/datasheets/discontinued/raspberry-pi/

### Sign up and log in Particle at https://www.particle.io

### Install the Particle-Agent on Raspberry Pi, log in the Particle account, and claim Raspberry Pi to the Particle account
```sh
$ bash <( curl -sL https://particle.io/install-pi )
```
### Download and open Particle Mobile App on a smartphone

### Log in Particle account and select Raspberry Pi

### Tinker > D7 > digitalWrite() > HIGH or LOW to toggle the green activity LED

### Alternatively, install Particle CLI and export /home/pi/bin to the shell PATH
```sh
$ bash <( curl -sL https://particle.io/install-cli )
$ export PATH="/home/pi/bin:$PATH"
$ particle login
$ particle call <device_name> digitalwrite D7=HIGH
$ particle call <device_name> digitalwrite D7=LOW
$ particle logout
```
## Lab B: Node.js

### Run Node.js server at http://127.0.0.1:8080 on Raspberry Pi
```sh
$ node -h
$ node -v
$ cd ~/iot/lesson6
$ node hello.js
$ node http.js
```
