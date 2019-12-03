# Source: https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
# 2019-11-27: tested with Raspberry Pi 4B, 6V power supply from a 4xAA battery holder, and the following servo motors
# TowerPro SG90 http://www.towerpro.com.tw/product/sg90-7
# Emax ES3001 https://emaxmodel.com/es3001-43g-analog-servo.html
# Parallax Continuous Rotation Servo https://www.parallax.com/product/900-00008
# 2019-12-03: tested with Raspberry Pi 4B, 6V power supply from a 4xAA battery holder, and the following servo motor
# Emax ES08A II https://emaxmodel.com/es08a-ii.html
import RPi.GPIO as GPIO
import time

servoPIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 22 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
