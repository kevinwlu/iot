# <a href="https://goo.gl/F0H9jW">Lesson 3</a>: Python

## Lab A: Python

### On a Raspberry Pi, install packages, update the IoT repository, and run python programs
```sh
$ sudo pip3 install -U jdcal astral geopy
$ cd iot
$ git pull
$ cd lesson3
$ python3 julian.py
$ python3 date_example.py
$ python3 datetime_example.py
$ python3 time_example.py
$ python3 sun.py 'New York'
$ python3 moon.py
$ python3 coordinates.py 'SC Williams Library'
$ python3 address.py '40.7448397, -74.02531776875'
$ python3 system_info.py
```
### Run socket server from a Terminal, and run socket client from ANOTHER Terminal of the same Raspberry Pi or a different one on the same subnetwork
```sh
$ python3 socket_server.py
$ python3 socket_client.py '155.246.x.x'
```
## Lab B: Breadboard

### 1. Connect the breadboard to Raspberry Pi 3V3, GND, GPIO 18, GPIO 24, and GPIO 25 using five DuPont male-to-female jump wires

### 2. Run the following three python programs
```sh
$ sudo python3 blink.py
$ sudo python3 manual.py
$ sudo python3 auto.py
```
### 3. Copy, edit (replace GMAIL_ADDRESS, RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD), and run the following two python programs
```sh
$ mkdir demo
$ cd demo
$ cp ~/iot/lesson3/test_email.py .
$ nano test_email.py
$ python3 test_email.py
$ cp ~/iot/lesson3/hello.py .
$ nano hello.py
$ sudo python3 hello.py
```
## Lab C: Remote GPIO

### 1. Launch the pigpio daemon using the −n flag to allow connections from a specific IP address of a controlling computer
```sh
pi@raspberrypi:~ $ sudo pigpiod -n <CONTROLLING_ADDRESS>
```
### 2. If the controlling computer uses other Linux distributions, macOS, or Windows, install GPIO Zero and pigpio, git clone the iot repository, go to the iot/lesson3 directory, and run the Python program with the environment variable PIGPIO_ADDR set to the IP address of the controlled Raspberry Pi
```sh
$ sudo pip3 install gpiozero pigpio
$ git clone https://github.com/kevinwlu/iot.git
$ cd ~/iot/lesson3
$ PIGPIO_ADDR=<CONTROLLED_ADDRESS> python3 led.py
```
### 3. If the controlling computer is another Raspberry Pi, go to the iot/lesson3 directory and run the Python program with the environment variables GPIOZERO_PIN_FACTORY set to pigpio since the default pin factory is RPi.GPIO
```sh
$ GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=<CONTROLLED_ADDRESS> python3 led.py
```
## Lab D: 1-Wire

### Connect DS18B20 to Raspberry Pi and run the Python program:

* GND to GND
* VDD to 3.3V or 5V
* DQ to GPIO 4 (the 4th pin from the left of the bottom row) and through a 4.7kΩ resistor to VDD
```h
pi@raspberrypi ~/iot/lesson3 $ sudo python3 temperature.py
```

## Lab E: Pypy
```sh
$ cd pypy
$ gcc -o test test.c
$ time ./test
$ time pypy test.py
$ time python test.py
$ time python3 test.py
$ pypy -m cProfile test.py
$ python -m cProfile test.py
$ python3 -m cProfile test.py
```
## Lab F: Doxygen
```sh
$ sudo apt install doxygen html2text
$ cd demo
$ cp ~/iot/lesson3/pyexample.py .
$ doxygen -g doxygen.config
$ nano doxygen.config
$ doxygen doxygen.config
$ cd html
$ html2text annotated.html
```
