import RPi.GPIO as GPIO
import time
import spidev

# Moisture sensor channel on MCP3008
moisture_channel = 2

GPIO.setmode(GPIO.BCM)
TRIGGER_PIN = 18
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
threshold = 100

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to read sensor connected to MCP3008
def readMoisture():
    level = 1023 - ReadChannel(moisture_channel)
    return level

# Controller main function
def runController():
    level = readMoisture()

# If the moisture level is lower/higher than the threshold, turn on/off the actuators
    if (level < threshold):
        GPIO.output(TRIGGER_PIN, True)
    else:
        GPIO.output(TRIGGER_PIN, False)

    print("Moisture: %s" % level)

while True:
    try:
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()    
