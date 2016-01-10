import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    try:
        GPIO.output(18, True)
        sleep(1)
        GPIO.output(18, False)
        sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
