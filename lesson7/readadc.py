import RPi.GPIO as GPIO
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the GPIO Pins on the Raspi

# MCP3008 to Raspi Pin connections
class PINS:
    SPICLK = 11
    SPIMOSI = 10
    SPIMISO = 9
    SPICS = 8

 # set up the SPI interface pins
def initialize():
    """
    Initializes the usb mode.

    Args:
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PINS.SPICLK, GPIO.OUT)
    GPIO.setup(PINS.SPIMOSI, GPIO.OUT)
    GPIO.setup(PINS.SPIMISO, GPIO.IN)
    GPIO.setup(PINS.SPICS, GPIO.OUT)

# Function to read data from Analog Pin 1 from MCP3008
# This function will be called in our loop to get the current sensor value
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    """
    Read an adcnum

    Args:
        adcnum: (int): write your description
        clockpin: (todo): write your description
        mosipin: (todo): write your description
        misopin: (str): write your description
        cspin: (todo): write your description
    """
    if ((adcnum > 7) or (adcnum < 0)):
            return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
            if (commandout & 0x80):
                    GPIO.output(mosipin, True)
            else:
                    GPIO.output(mosipin, False)
            commandout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
            adcout <<= 1
            if (GPIO.input(misopin)):
                    adcout |= 0x1

    GPIO.output(cspin, True)

    adcout /= 2       # first bit is 'null' so drop it
    return adcout
