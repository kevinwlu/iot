import time
from adxl345 import ADXL345

adxl345 = ADXL345()
print("ADXL345 on address 0x%x:" % (adxl345.address))

def runController():
    axes = adxl345.getAxes(True)
    print('x = %.3f y = %.3f z = %.3f' % (axes['x'], axes['y'], axes['z']))

while True:
    runController()
    time.sleep(5)
