import RPi.GPIO as GPIO
import time
import spidev

# Moisture sensor channel on MCP3008
moisture_channel = 0

GPIO.setmode(GPIO.BCM)
TRIGGER_PIN = 18
threshold = 10

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    """
    Read a channel.

    Args:
        channel: (todo): write your description
    """
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to read sensor connected to MCP3008
def readMoisture():
    """
    Reads a channel from the channel.

    Args:
    """
    level = ReadChannel(moisture_channel)
    return level

# Controller main function
def runController():
    """
    Run the logging information.

    Args:
    """
    level = readMoisture()

# Check moisture level
    if (level < threshold):
        GPIO.output(TRIGGER_PIN, True)
    else:
        GPIO.output(TRIGGER_PIN, False)

    print("Moisture: %s" % level)

while True:
    runController()
    time.sleep(10)
