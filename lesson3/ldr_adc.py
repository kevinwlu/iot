import spidev
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000
adc=spi.xfer2([1, 8<<4, 0])
print('adc = ', adc)
data=((adc[1]&3)<<8)+adc[2]
print('data = ', data)
spi.close()
