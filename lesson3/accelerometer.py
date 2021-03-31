# https://learn.sparkfun.com/tutorials/adxl345-hookup-guide/all
# https://pimylifeup.com/raspberry-pi-accelerometer-adxl345/
# sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
# sudo i2cdetect -y 1
# sudo pip3 install adafruit-circuitpython-ADXL34x
# python3 accelerometer.py
import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)
