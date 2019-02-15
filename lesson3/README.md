# <a href="https://goo.gl/F0H9jW">Lesson 3</a>: Python

## Lab A: Python

### On a Raspberry Pi, install packages, update the IoT repository, and run python programs

sudo pip3 install -U jdcal astral geopy

cd iot

git pull

cd lesson3

python3 julian.py

python3 date_example.py

python3 datetime_example.py

python3 time_example.py

python3 sun.py 'New York'

python3 moon.py

python3 coordinates.py 'SC Williams Library'

python3 address.py '40.7448397, -74.02531776875'

python3 system_info.py

### Run socket server from a Terminal, and run socket client from another Terminal of the same Raspberry Pi or a different one on the same subnetwork

python3 socket_server.py

python3 socket_client.py '155.246.x.x'

## Lab B: Breadboard

### 1. Connect the breadboard to Raspberry Pi 3V3, GND, GPIO 18, GPIO 24, and GPIO 25 using five DuPont male-to-female jump wires

### 2. Run the following three python programs

sudo python3 blink.py

sudo python3 manual.py

sudo python3 auto.py

### 3. Copy, edit (replace GMAIL_ADDRESS, RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD), and run the following two python programs

mkdir demo

cd demo

cp ~/iot/lesson3/test_email.py .

nano test_email.py

python3 test_email.py

cp ~/iot/lesson3/hello.py .

nano hello.py

sudo python3 hello.py

## Lab C: Pypy

cd pypy

gcc -o test test.c

time ./test

time pypy test.py

time python test.py

time python3 test.py

pypy -m cProfile test.py

python -m cProfile test.py

python3 -m cProfile test.py

## Lab D: Doxygen

sudo apt-get install doxygen

cd demo

cp ~/iot/lesson3/pyexample.py .

doxygen -g doxygen.config

nano doxygen.config

doxygen doxygen.config
