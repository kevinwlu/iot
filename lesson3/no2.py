import time
import spidev

# Sensor channel on MCP3008
#CO_CHANNEL = 0
NO2_CHANNEL = 1

vin = 5
r0 = 10000
pullup = 10000

# Conversions based on Rs/Ro vs ppm plots of the sensors
#CO_Conversions = [((0, 100), (0, 0.25)), ((100, 133), (0.25, 0.325)),
#    ((133, 167), (0.325, 0.475)), ((167, 200), (0.475, 0.575)),
#    ((200, 233), (0.575, 0.665)), ((233, 267), (0.666, 0.75))]
NO2_Conversions = [((0, 100), (0, 0.25)), ((100, 133), (0.25, 0.325)),
    ((133, 167), (0.325, 0.475)), ((167, 200), (0.475, 0.575)),
    ((200, 233), (0.575, 0.665)), ((233, 267), (0.666, 0.75))]

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Function to read SPI data from MCP3008 chip
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def get_resistance(channel):
    result = ReadChannel(channel)
    if result == 0:
        resistance = 0
    else:
        resistance = (vin/result -1) * pullup
    return resistance

def converttoppm(rs, conversions):
    rsper = 100 * (float(rs) / r0)
    for a in conversions:
        if a[0][0] >= rsper > a[0][1]:
            mid, hi = rsper - a[0][0], a[0][1] - a[0][0]
            sf = float(mid) / hi
            ppm = sf * (a[1][1] - a[1][0]) + a[1][0]
            return ppm
        return 0

def get_NO2():
    rs = get_resistance(NO2_CHANNEL)
    ppm = converttoppm(rs, NO2_Conversions)
    return ppm

#def get_CO():
#    rs = get_resistance(CO_CHANNEL)
#    ppm = converttoppm(rs, CO_Conversions)
#    return ppm

# Controller main function
def runController():
    NO2_reading = get_NO2()
#    CO_reading = get_CO()
#    print('CO={0:0.5f} ppm  NO2={1:0.5f} ppm'.format(CO_reading, NO2_reading))
    print('NO2={:0.5f} ppm'.format(NO2_reading))

while True:
    runController()
    time.sleep(10)
