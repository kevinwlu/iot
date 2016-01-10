from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Switch Pin
GPIO.setup(25, GPIO.IN)

# LED Pin
GPIO.setup(18, GPIO.OUT)

state = False

def toggleLED(pin):
    global state
    state = not state
    GPIO.output(pin, state)

while True:
    try:
        if(GPIO.input(25) == True):
            toggleLED(18)
        sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
