# Lesson 3: Python

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)
  * [CPython](https://en.wikipedia.org/wiki/CPython)
  * [Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))
  * [Jupyter](https://en.wikipedia.org/wiki/Project_Jupyter)
  * [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation) (PSF)
  * [PyPI](https://en.wikipedia.org/wiki/Python_Package_Index) (Python Package Index))
  * [Keyboard interrupt](https://en.wikipedia.org/wiki/Keyboard_interrupt)
  * [Control-C](https://en.wikipedia.org/wiki/Control-C)
* [Bitwise operators](https://wiki.python.org/moin/BitwiseOperators)
* [pip](https://en.wikipedia.org/wiki/Pip_(package_manager))
  * [Setuptools](https://en.wikipedia.org/wiki/Setuptools)
  * [2to3](https://docs.python.org/3/library/2to3.html)
  * [Astral](https://astral.readthedocs.io/en/latest/)
  * [GeoPy](https://geopy.readthedocs.io/en/stable/)
  * [psutil](https://pypi.org/project/psutil/)
* [Unicode](https://en.wikipedia.org/wiki/Unicode)
* [GPIO Zero](https://gpiozero.readthedocs.io/en/stable)
* [pigpio](http://abyz.me.uk/rpi/pigpio)
* [PyPy](https://en.wikipedia.org/wiki/PyPy)
* [MicroPython](https://en.wikipedia.org/wiki/MicroPython)
* [CircuitPython](https://en.wikipedia.org/wiki/CircuitPython)
* [Doxygen](https://en.wikipedia.org/wiki/Doxygen)

## Lab 3A: Python

* [APT](https://en.wikipedia.org/wiki/APT_(software)) is used to install software on GNU/Linux such as Raspberry Pi OS
  * [Chocolatey](https://chocolatey.org/) may be used to install software on Windows
  * [Homebrew](https://brew.sh/) may be used to install software on macOS
* [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) is used to install Python packages on GNU/Linux, macOS , or Windows
* If Python has not been installed on Windows, [download](https://www.python.org/downloads/windows/) and install the latest version of Python 3
* On Windows, edit path in "System Properties > Advanced > Environment Variables" and add 
```sh  
C:\Users\...\AppData\Local\Programs\Python\Python... 
C:\Users\...\AppData\Local\Programs\Python\Python...\Scripts
```
* Open Command Promt or PowerShell on Windows, enter python
  * Alternatively, download and open [Git for Windows](https://gitforwindows.org/), enter python -i
  * To SSH Raspberry Pi, join the [Windows Insiders Program](https://insider.windows.com/en-us/getting-started) and install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL)
* Numbers: int, float, and complex
```sh
$ python
>>> a=3
>>> a
>>> type(a)
>>> x=2.1
>>> x;type(x)
>>> a+x
>>> a-x
>>> a*x
>>> x/a
>>> a**2
>>> y=2+3j
>>> y;type(y)
>>> y.real
>>> y.imag
```
* Strings: text and binary data
```sh
>>> s='Hello World!'
>>> type(s)
>>> s.upper()
>>> s.lower()
>>> s.strip('!')
>>> s[0]
>>> s[6:]
>>> s[6:-1]
>>> len(s)
>>> b=s.encode()
>>> b
>>> type(b)
>>> c=b.decode()
>>> c
>>> type(c)
>>> t=' This is a simple program.'
>>> s+t
>>> print('"{:s}" has {:d} characters.'.format(s, len(s)))
```
* Tuples
```sh
>>> veggies=('beet', 'corn', 'kale')
>>> type(veggies)
>>> len(veggies)
>>> veggies[0:2]
>>> veggies+('leek', 'okra')
```
* Lists
```sh
>>> fruits=['apple', 'banana', 'mango']
>>> type(fruits)
>>> len(fruits)
>>> fruits[0:2]
>>> fruits+['orange', 'papaya']
>>> fruits.append('orange')
>>> fruits
>>> fruits.remove('mango')
>>> fruits
>>> fruits.insert(1, 'mango')
>>> fruits
```
* Dictionaries
```sh
>>> student={'name': 'Mary', 'id': '8776'}
>>> type(student)
>>> student['name']
>>> student.items()
>>> student.keys()
>>> student.values()
>>> students={'1': {'name': 'Alex', 'grade': 3.8}, 
...           '2': {'name': 'Barb', 'grade': 2.5}, 
...           '3': {'name': 'Dave', 'grade': 4.2},
...           '4': {'name': 'John', 'grade': 4.1},
...           '5': {'name': 'Mary', 'grade': 3.5}}
>>> students.keys()
```
* If else
```sh
>>> z=25**5
>>> if z>1000000:
...     print('More')
... else:
...     print('Less')
...
```
* If not
```sh
>>> if not 'major' in student.keys():
...     student['major']='ECE'
...
>>> student
```
* For
```sh
>>> for v in s:
...     print(v, end=' ')
...
>>> i=0
>>> for item in fruits:
...     print('Fruit {:d}: {:s}'.format(i, item))
...     i=i+1
...
>>> for key in student:
...     print('{:s}: {:s}'.format(key, student[key]))
...
```
* While
```sh
>>> i=0
>>> while i<=10:
...     if i%2==0:
...         print(i, end=' ')
...     i=i+1
...
```
* Break
```sh
>>> m=1
>>> for n in range(4, 256, 4):
...     m=m*n
...     if m>512:
...         break
...     print(m)
...
```
* Continue (or pass)
```sh
>>> grains=['oat', 'rice', 'rye', 'wheat']
>>> for item in grains:
...     if item=='rice':
...         continue
...     else:
...         print(item, end=' ')
...
```
* Mathematical functions
```sh
>>> import math
>>> math.ceil(1.5)
>>> math.floor(1.5)
>>> math.factorial(10)
>>> math.fmod(10,3)
>>> 10%3
>>> math.sqrt(64)
>>> math.exp(1)
>>> math.log(4,2)
>>> math.degrees(1.5707963267948966)
>>> math.radians(90)
>>> math.asin(1)
>>> math.sin(1.5707963267948966)
>>> math.cos(math.pi)
```
* [Built-in functions](https://docs.python.org/3/library/functions.html)
```sh
>>> r=range(10)
>>> r
>>> r[::-1]
>>> r[::2]
>>> r[1::3]
>>> range(10, 110, 10)
```
* Defining functions
```sh
>>> def printList(list):
...     print('{:d} items on the list:'.format(len(list)))
...     for item in list:
...         print(item, end=' ')
...
>>> def averageGrade(dict):
...     sum=0.0
...     for key in dict:
...         sum=sum+dict[key]['grade']
...     average=sum/len(dict)
...     return average
...
>>> averageGrade(students)
>>> exit()
```
* Keyword arguments
```sh
>>> def printID(name, **kwargs):
...     print('Student Name: ', name, sep='')
...     for key in kwargs:
...         print(key, ': ', kwargs[key], sep='')
...
>>> printID(name='Mary', id='8776', major='ECE')
```
* Variable-length arguments
```sh
>>> def printID(name, *varargs):
...     print('Student Name:', name)
...     for item in varargs:
...         print(item)
...
>>> printID('Barb')
>>> printID('Mary', 'id: 8776', 'major: ECE')
>>> exit()
```
* Modules
  * If haven't done so, clone the IoT repository
```sh
$ cd
$ git clone https://github.com/kevinwlu/iot.git
$ cd iot
$ cd lesson3
$ python
>>> import student
>>> students={'1':{'name':'Alex','grade':3.8},
...           '2':{'name':'Barb','grade':2.5}, 
...           '3':{'name':'Dave','grade':4.2},
...           '4':{'name':'John','grade':4.1},
...           '5':{'name':'Mary','grade':3.5}}
>>> student.printRecords(students)
>>> avg=student.averageGrade(students)
>>> print('The average is {:0.2f}'.format(avg))
>>> from student import averageGrade
>>> avg=averageGrade(students)
>>> print('The average is {:0.2f}'.format(avg))
```
* Read and write files
```sh
>>> fp=open('file.txt', 'r')
>>> content=fp.read()
>>> print(content)
>>> fp.close()
>>> exit()
$ cd
$ mkdir demo
$ cd demo
$ python
>>> fo=open('file1.txt', 'w')
>>> content='This is an example of writing to a file in Python.'
>>> fo.write(content)
>>> fo.close()
>>> exit()
$ cat file1.txt
```
* Install/upgrade Python packages with pip
```sh
$ python -m pip install --upgrade pip
$ pip install 2to3 jdcal astral geopy psutil
$ cd
$ cd iot/lesson3
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
$ python cpu.py
$ python battery.py
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
$ python3 cpu.py
$ python3 battery.py
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

### 1. Connect the breadboard components (including a 1&mu;F capacitor) to Raspberry Pi 3V3, GND, GPIO 18, GPIO 24, and GPIO 25 using five jump wires

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
