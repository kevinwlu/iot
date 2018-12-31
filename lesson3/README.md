# <a href="https://goo.gl/F0H9jW">Lesson 3</a>: Python

# Install Jdcal to convert between Julian dates and calendar dates

sudo pip3 install -U jdcal

python3 julian.py

python3 date_example.py

python3 datetime_example.py

python3 time_example.py

# Install Astral to calculate the times of various aspects of the sun and moon

sudo pip3 install -U astral

python3 sun.py 'New York'

python3 moon.py

# Install GeoPy to locate the coordinates of addresses, cities, countries, and landmarks

sudo pip3 install -U geopy

python3 coordinates.py 'SC Williams Library'

python3 address.py '40.7448397, -74.02531776875'

# Run socket server from a Terminal, and run socket client from another Terminal

python3 socket_server.py

python3 socket_client.py '155.246.x.x'

# Run Python code with a breadboard

sudo python3 blink.py

sudo python3 manual.py

sudo python3 auto.py

# Copy, edit (replace GMAIL_ADDRESS, RECIPIENT_EMAIL, GMAIL_USERNAME, and GOOGLE_APP_PASSWORD), and run the following two python programs

mkdir demo

cd demo

cp ~/iot/lesson3/test_email.py .

nano test_email.py

python3 test_email.py

cp ~/iot/lesson3/hello.py .

nano hello.py

sudo python3 hello.py

# Run speed comparisons

cd pypy

gcc -o test test.c

time ./test

time pypy test.py

time python test.py

time python3 test.py

pypy -m cProfile test.py

python -m cProfile test.py

python3 -m cProfile test.py

# Install Doxygen, generate and edit configuration file, and generate documentation

sudo apt-get install doxygen

cd demo

cp ~/iot/lesson3/pyexample.py .

doxygen -g doxygen.config

nano doxygen.config

doxygen doxygen.config
