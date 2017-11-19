# <a href="https://goo.gl/hRoMYW">Lesson 2</a>: Raspberry Pi

# Install and run fswebcam to use a USB webcam

sudo apt-get update

sudo apt-get install fswebcam

fswebcam image.jpg

fswebcam -r 1280x720 image2.jpg

fswebcam -r 1280x720 --no-banner image3.jpg

# Install and run minicom

sudo nano /boot/cmdline.txt

sudo apt-get install minicom

minicom –b 115200 –o –D /dev/ttyS0

minicom –b 9600 –o –D /dev/ttyS0

minicom -b 9600 -o -D /dev/ttyAMA0

# Install python-dev and spidev

sudo apt-get install python-dev

sudo pip install -U pip

sudo pip install -U spidev

# Switch an LED on/off

sudo su

echo 18 > /sys/class/gpio/export

cd /sys/class/gpio/gpio18

echo out > direction

echo 1 > value

echo 0 > value

cd /home/pi

echo 18 > /sys/class/gpio/unexport

exit

# Install i2c-tools and python-smbus to test I2C addresses in use

sudo apt-get install i2c-tools python-smbus

sudo i2cdetect -y 1

