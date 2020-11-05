import time
import datetime
import sqlite3
import spidev
import RPi.GPIO as GPIO

# Initialize SQLite
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

# LDR channel on MCP3008
LIGHT_CHANNEL = 0

# GPIO Setup
GPIO.setmode(GPIO.BCM)
LIGHT_PIN = 25

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

# Light Level Threshold
threshold = 100

# Function to read LDR connected to MCP3008
def readLDR():
    """
    Read lux light light light.

    Args:
    """
    light_level = ReadChannel(LIGHT_CHANNEL)
    if light_level == 0:
        lux = 0
    else:
        lux = ConvertLux(light_level, 2)
    return lux

# Function to convert LDR reading to Lux
def ConvertLux(data, places):
    """
    Convert the volume of a given a lux ).

    Args:
        data: (array): write your description
        places: (list): write your description
    """
    R = 10 #10k-ohm resistor connected to LDR
    volts = (data * 3.3) / 1023
    volts = round(volts, places)
    lux = 500 * (3.3 - volts) / (R * volts)
    return lux

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    """
    Read a channel.

    Args:
        channel: (todo): write your description
    """
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# Get current mode from DB
def getCurrentMode():
    """
    Returns the current database.

    Args:
    """
    cur.execute('SELECT * FROM myapp_mode')
    data = cur.fetchone()  # (1, 'auto')
    return data[1]

# Get current state from DB
def getCurrentState():
    """
    Returns the current state of the currently running state.

    Args:
    """
    cur.execute('SELECT * FROM myapp_state')
    data = cur.fetchone()  # (1, 'on')
    return data[1]

# Store current state in DB
def setCurrentState(val):
    """
    Sets the current state.

    Args:
        val: (todo): write your description
    """
    query = 'UPDATE myapp_state set name = "'+val+'"'
    cur.execute(query)

def switchOnLight(PIN):
    """
    Takes an output of the switch.

    Args:
        PIN: (int): write your description
    """
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

def switchOffLight(PIN):
    """
    Sets the output of the switch.

    Args:
        PIN: (int): write your description
    """
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)

def runManualMode():
    """
    Run the switch.

    Args:
    """
    # Get current state from DB
    currentState = getCurrentState()
    if currentState == 'on':
        print('Manual - On')
        switchOnLight(LIGHT_PIN)
    elif currentState == 'off':
        print('Manual - Off')
        switchOffLight(LIGHT_PIN)

def runAutoMode():
    """
    Run the lightlevel.

    Args:
    """
    # Read LDR
    lightlevel = readLDR()
    if lightlevel < threshold:
        print('Auto - On (lux=%d)' % lightlevel)
        switchOnLight(LIGHT_PIN)
    else:
        print('Auto - Off (lux=%d)' % lightlevel)
        switchOffLight(LIGHT_PIN)

# Controller main function
def runController():
    """
    Returns whether or not the current run is running.

    Args:
    """
    currentMode = getCurrentMode()
    if currentMode == 'auto':
        runAutoMode()
    elif currentMode == 'manual':
        runManualMode()
    return True

while True:
    try:
        runController()
        time.sleep(5)
    except KeyboardInterrupt:
        spi.close()
        GPIO.cleanup()
        exit()
