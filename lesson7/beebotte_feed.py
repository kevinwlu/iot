import time
import board
import adafruit_dht
from beebotte import *
bbt = BBT('API_KEY', 'SECRET_KEY')
period = 60 # seconds
#pin = 24
dhtDevice = adafruit_dht.DHT22(board.D24)
temp_resource = Resource(bbt, 'RaspberryPi', 'temperature')
humid_resource = Resource(bbt, 'RaspberryPi', 'humidity')
def run():
    """
    Run the humidity.

    Args:
    """
    while True:
#        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
        humidity = dhtDevice.humidity
        temperature = dhtDevice.temperature
        if humidity is not None and temperature is not None:
            print("Temp={0:f}*C  Humidity={1:f}%".format(temperature, humidity))
            try:
                temp_resource.write(temperature)
                humid_resource.write(humidity)
            except Exception:
                print("Error while writing to Beebotte")
        else:
            print("Failed to get reading. Try again!")
        time.sleep(period)
while True:
    try:
        run()
    except KeyboardInterrupt:
        exit()
