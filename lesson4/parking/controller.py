import RPi.GPIO as GPIO
import time
import sys
import requests

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17
TRIGGER_PIN = 18
threshold = 10

def readUltrasonicSensor():
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)
    while GPIO.input(SENSOR_PIN) == 0:
        signaloff = time.time()
    while GPIO.input(SENSOR_PIN) == 1:
        signalon = time.time()
    timepassed = signalon - signaloff
    distance = timepassed * 17000
    if distance < threshold:
        return 1
    else:
        return 0

def runController():
    pinState = readUltrasonicSensor()
    if pinState == 1:
        print('Occupied')
        setCurrentState('occupied')
    else:
        print('Empty')
        setCurrentState('empty')

def setCurrentState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/state/1/', data=values,
                     auth=('pi', 'raspberry'))

while True:
    try:
        runController()
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
