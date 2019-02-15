# <a href="https://goo.gl/hRoMYW">Lesson 2</a>: Raspberry Pi

## Lab A: Serial

### 1. On the SSH Terminal, enter "sudo nano /boot/cmdline.txt"

* Delete "console=serial0,115200" if found

* Save the file with control-x y enter

* Enter "sudo reboot"

### 2. Connect two serial pins (the 4th and 5th pins from the left of the top row) using one DuPont female-to-female jump wire

* Enter "sudo apt-get install minicom"

* Enter "minicom -b 115200 -o -D /dev/ttyS0" for serial loopback test by typing

control-a a (to enable new line) then hello

control-a e (to enable echo) then hello

control-a x (to exit)

### 3. Optionally, perform serial test between two Raspberry Pi's using three DuPont female-to-female jump wires

* Connect TX of a Raspberry Pi to RX of the other

* Connect GND of both Raspberry Pi's

## Lab B: SPI and I2C

### 1. Connect the SPI MOSI and MISO pins (the 10th and 11th pins from the left of the bottom row) using one DuPont female-to-female jump wire, and enter the following three commands on an SSH Terminal:

wget https://raw.githubusercontent.com/raspberrypi/linux/rpi-3.10.y/Documentation/spi/spidev_test.c

gcc -o spidev_test spidev_test.c

./spidev_test -D /dev/spidev0.0

### 2. Connect 3V3, GND, SDA, and SCL using four DuPont female-to-female jump wires with I2C devices (ADXL345 and BMP180), install i2c-tools, and test I2C addresses (53 and 77) in use on an SSH Terminal:

sudo apt-get install i2c-tools python-smbus

sudo i2cdetect -y 1

## Lab C: Fritzing

### 1. On laptop, download Fritzing (before the class since it takes time), install, and run 

### 2. Click Breadboard, drag and drop parts including Raspberry Pi, LED, and resistor

### 3. Click File menu, save the file, and export as image

## Lab D: GPIO and LED

### 1. Connect an LED on a breadboard to the Raspberry Pi GPIO using two DuPont male-to-female jump wires as shown in Lab C

### 2. On a Terminal, enter the following commands to switch an LED on/off 

pi@iotus:~ $ sudo su

root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/export

root@raspberypi:/home/pi# cd /sys/class/gpio/gpio18

root@raspberypi:/sys/class/gpio/gpio18# echo out > direction

root@raspberypi:/sys/class/gpio/gpio18# echo 1 > value

root@raspberypi:/sys/class/gpio/gpio18# echo 0 > value

root@raspberypi:/sys/class/gpio/gpio18# cd /home/pi

root@raspberypi:/home/pi# echo 18 > /sys/class/gpio/unexport

root@raspberypi:/home/pi# exit

exit

pi@iotus:~ $

## Lab E: USB Webcam

#### Connect a USB webcam, install fswebcam, and save images:

sudo apt-get update

sudo apt-get install fswebcam

fswebcam image.jpg

fswebcam -r 1280x720 image2.jpg

fswebcam -r 1280x720 --no-banner image3.jpg
