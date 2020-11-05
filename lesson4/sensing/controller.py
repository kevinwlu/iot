import RPi.GPIO as GPIO
import time
import sys
import requests

GPIO.setmode(GPIO.BCM)
ROOM_SENSOR_PIN = 27
DOOR_SENSOR_PIN = 23
GPIO.setup(ROOM_SENSOR_PIN, GPIO.IN)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def readingRoomSensor():
    """
    Return the number of threads.

    Args:
    """
    if GPIO.input(ROOM_SENSOR_PIN):
        print('motion detected')
        return 1
    else:
        return 0

def readingDoorSensor():
    """
    Return the number of threads.

    Args:
    """
    if GPIO.input(DOOR_SENSOR_PIN):
        print('door opened')
        return 1
    else:
        return 0

def runController():
    """
    Run a new session.

    Args:
    """
    roomState = readingRoomSensor()
    if roomState == 1:
        setRoomState('yes')
    else:
        setRoomState('no')
    doorState = readingDoorSensor()
    if doorState == 1:
        setDoorState('open')
    else:
        setDoorState('closed')

def setRoomState(val):
    """
    Set the state of the led.

    Args:
        val: (float): write your description
    """
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/room/1/', data=values, auth=('pi', 'raspberry'))

def setDoorState(val):
    """
    Sets whether or off of the led mode.

    Args:
        val: (float): write your description
    """
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/door/1/', data=values, auth=('pi', 'raspberry'))

while True:
    try:
        runController()
        time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
