import time
import spidev
channel = 0

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
def readMQ():
    level = ReadChannel(channel)
    return level

# Controller main function
def runController():
    level = readMQ()
    print('level={0:0.5f}'.format(level))

while True:
    try:
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
