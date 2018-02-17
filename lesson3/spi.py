import sys
import spidev
channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000
adc = spi.xfer2([1, (8 + channel) << 4, 0])
print('adc = ', adc)
data = ((adc[1]&3) << 8) + adc[2]
print('data = ', data)
R = 10
places = 2
volts = (data * 3.3) / 1023
volts = round(volts, places)
print('volts = ', volts)
if volts == 0:
    lux = 0
else:
    lux = 500 * (3.3 - volts) / (R * volts)
print('lux = ', lux)
spi.close()
