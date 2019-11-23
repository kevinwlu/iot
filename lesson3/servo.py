# Servo Control
# sudo pip3 install wiringpi
# https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor/overview
# http://www.towerpro.com.tw/product/sg90-7
import time
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01
 
while True:
        for pulse in range(50, 250, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
