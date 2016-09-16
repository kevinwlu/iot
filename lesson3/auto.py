import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ldr_threshold = 1000
LDR_PIN = 24
LIGHT_PIN = 18

def readLDR(PIN):
    count = 0
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)
    time.sleep(0.1)
    GPIO.setup(PIN, GPIO.IN)
    while (GPIO.input(PIN) == False):
        count = count + 1
    return count

def switchOnLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

def switchOffLight(PIN):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)

while True:
    try:
        ldr_reading = readLDR(LDR_PIN)
        print(ldr_reading)
        if ldr_reading > ldr_threshold:
            switchOnLight(LIGHT_PIN)
        else:
            switchOffLight(LIGHT_PIN)
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
