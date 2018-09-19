# <a href="https://goo.gl/hRoMYW">Lesson 2</a>: Raspberry Pi

# Install and run fswebcam to use a USB webcam

sudo apt-get update

sudo apt-get install fswebcam

fswebcam image.jpg

fswebcam -r 1280x720 image2.jpg

fswebcam -r 1280x720 --no-banner image3.jpg

# Serial Loopback Test

sudo nano /boot/cmdline.txt

sudo apt-get install minicom

minicom –b 115200 –o –D /dev/ttyS0

minicom –b 9600 –o –D /dev/ttyS0

# SPI Loopback Test

wget https://raw.githubusercontent.com/raspberrypi/linux/rpi-3.10.y/Documentation/spi/spidev_test.c

gcc -o spidev_test spidev_test.c

./spidev_test -D /dev/spidev0.0

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

# Test I2C Addresses in Use

sudo apt-get install i2c-tools python-smbus

sudo i2cdetect -y 1
