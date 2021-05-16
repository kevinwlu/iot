# Lesson 3: Python

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [CPython](https://en.wikipedia.org/wiki/CPython)
  * [Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))
  * [Keyboard interrupt](https://en.wikipedia.org/wiki/Keyboard_interrupt)
  * [Control-C](https://en.wikipedia.org/wiki/Control-C)
* [2to3](https://docs.python.org/3/library/2to3.html)
* [pip](https://en.wikipedia.org/wiki/Pip_(package_manager))
* [Unicode](https://en.wikipedia.org/wiki/Unicode)
* [GPIO Zero](https://gpiozero.readthedocs.io/en/stable)
* [pigpio](http://abyz.me.uk/rpi/pigpio)
* [PyPy](https://en.wikipedia.org/wiki/PyPy)
* [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
* [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
* [Doxygen](https://en.wikipedia.org/wiki/Doxygen)

## Lab 3A: Python

* If Python has not been installed on Windows 10, [download](https://www.python.org/downloads/windows/) and install the latest version of Python 3
* On Windows 10, edit path in "System Properties > Advanced > Environment Variables" and add 
```sh  
C:\Users\...\AppData\Local\Programs\Python\Python... 
C:\Users\...\AppData\Local\Programs\Python\Python...\Scripts
```
* Open Git Bash on Windows 10, run Python and install/upgrade Python packages with pip
```sh
$ python -i
>>> import math
>>> math.sqrt(64)
8.0
>>> exit()
$ python -m pip install --upgrade pip
$ pip install jdcal astral geopy
$ cd
$ cd iot
$ git pull
$ cd lesson3
$ 2to3 2example.py
$ python julian.py
$ python date_example.py
$ python datetime_example.py
$ python time_example.py
$ python sun.py 'New York'
$ python sun.py 'Beijing'
$ python sun.py 'New Delhi'
$ python moon.py
$ python coordinates.py 'SC Williams Library'
$ python address.py '40.74480675, -74.02532862031404'
$ python documentstats.py document.txt
```
### NOTE: Raspberry Pi OS (or macOS/Linux) has both Python 2 and Python 3 already preinstalled
### WARNING: Don't upgrade the preinstalled Python or PIP on Raspberry Pi OS
* Run pip3 to install/upgrade packages, update the IoT repository, and run Python 3 programs
```sh
$ sudo pip3 install -U jdcal astral geopy
$ cd iot
$ git pull
$ cd lesson3
$ 2to3 2example.py
$ python3 julian.py
$ python3 date_example.py
$ python3 datetime_example.py
$ python3 time_example.py
$ python3 sun.py 'New York'
$ python3 sun.py 'Beijing'
$ python3 sun.py 'New Delhi'
$ python3 moon.py
$ python3 coordinates.py 'SC Williams Library'
$ python3 address.py '40.74480675, -74.02532862031404'
$ python3 documentstats.py document.txt
```
### On Raspberry Pi only
```sh
$ python3 system_info.py
```
### Run ifconfig on Raspberry Pi (macOS or Linux) or ipconfig on Windows to find IP address 
```sh
$ ifconfig
```
### Run [network socket](https://en.wikipedia.org/wiki/Network_socket) server from a Terminal, and run network socket client from ANOTHER Terminal of the same Raspberry Pi or a different one on the same subnetwork using the IP address as a string in single quotes
* 'The Server IP Address' is a placeholder to be replaced with a real IP address such as 192.168.1.200
```sh
$ python3 socket_server.py
$ python3 socket_client.py 'The Server IP Address'
```
## Lab 3B: Breadboard

### 1. Connect the breadboard components (including a 1&mu;F capacitor) to Raspberry Pi 3V3, GND, GPIO 18, GPIO 24, and GPIO 25 using five DuPont male-to-female jump wires

![ldr_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson3/ldr_bb.png)

### 2. Run the following three python programs
```sh
$ python3 blink.py
$ python3 manual.py
$ python3 auto.py
```
### 3. Make a new directory, copy files to the current directory (in a single dot as opposed to the parent directory in double dots), edit (replace GMAIL_ADDRESS, RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD)
* test_email.py doesn't require the breadboard
* hello.py requires a button to be pressed for sending an email
```sh
$ cd
$ mkdir demo
$ cd demo
$ cp ~/iot/lesson3/test_email.py .
$ nano test_email.py
$ python3 test_email.py
$ cp ~/iot/lesson3/hello.py .
$ nano hello.py
$ python3 hello.py
```
## Lab 3C: Remote GPIO

### 1. Launch the pigpio [daemon](https://en.wikipedia.org/wiki/Daemon_(computing)) using the −n flag to allow connections from a specific IP address of a controlling computer without quotation marks
```sh
pi@raspberrypi:~ $ sudo pigpiod -n <CONTROLLING_ADDRESS>
```
### 2. If the controlling computer is on macOS (sudo pip3 install) or Windows (pip install), install GPIO Zero and pigpio, git clone the iot repository, go to the iot/lesson3 directory, and run the Python program with the environment variable PIGPIO_ADDR set to the IP address of the controlled Raspberry Pi
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
## Lab 3D: 1-Wire

### Connect DS18B20 to Raspberry Pi and run the Python program:

* GND to GND
* VDD to 3.3V or 5V
* DQ to GPIO 4 (the 4th pin from the left of the bottom row) and through a 4.7k&Omega; resistor to VDD

![1-wire_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson3/1-wire_bb.png)

```h
pi@raspberrypi:~/iot/lesson3 $ python3 temperature.py
```

## Lab 3E: PyPy
```sh
$ cd ~/iot/lesson3/pypy
$ gcc -o test test.c
$ time ./test
$ time pypy test.py
$ time python test.py
$ time python3 test.py
$ pypy -m cProfile test.py
$ python -m cProfile test.py
$ python3 -m cProfile test.py
```
## Lab 3F: Doxygen
```sh
$ sudo apt install doxygen html2text
$ cd ~/demo
$ cp ~/iot/lesson3/pyexample.py .
$ doxygen -g doxygen.config
$ nano doxygen.config
```
> PROJECT_NAME           = "pyexample"

> OPTIMIZE_OUTPUT_JAVA   = YES
```sh
$ doxygen doxygen.config
$ cd html
$ html2text annotated.html
```
