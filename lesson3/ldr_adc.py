import spidev
spi=spidev.SpiDev()
spi.open(0,0)
adc=spi.xfer2([1, 8<<4, 0])
print adc
data=((adc[1]&3)<<8)+adc[2]
print data
