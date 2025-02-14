# Source: http://www.python-exemplary.com/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/servomotors.inc.php
# 2019-11-27: tested with Raspberry Pi 4B, 6V power supply from a 4xAA battery holder, and the following servo motors
# TowerPro SG90 http://www.towerpro.com.tw/product/sg90-7
# Emax ES3001 https://emaxmodel.com/es3001-43g-analog-servo.html
# Parallax Continuous Rotation Servo https://www.parallax.com/product/900-00008
# 2019-12-03: tested with Raspberry Pi 4B, 6V power supply from a 4xAA battery holder, and the following servo motor
# Emax ES08A II https://emaxmodel.com/es08a-ii.html

import RPi.GPIO as GPIO
import time

P_SERVO = 22 # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)
a = 10
b = 2

def setup():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)
    time.sleep(1) # allow to settle
   
print("starting")
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
GPIO.cleanup() 
print("done")
