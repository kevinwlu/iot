# Required installation of adafruit-blinka and CircuitPython-DHT library
# pip3 install adafruit-circuitpython-dht
# sudo apt update
# sudo apt install libgpiod2
# 
import time
import datetime
import board
import adafruit_dht
import paho.mqtt.client as mqtt
dhtDevice = adafruit_dht.DHT22(board.D24)
#mqttc = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
#client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.loop_start()
while True:
    try:  
        humidity = dhtDevice.humidity
        temp = dhtDevice.temperature
        if humidity is None or temp is None:
            time.sleep(2)
            continue
        now = datetime.datetime.now()
        dt = now.replace(microsecond=0)
        print(dt)
        print('Temperature: {0:0.1f} C'.format(temp))
        print('Humidity:    {0:0.1f} %'.format(humidity))
        mqttc.publish("rpi/dht", "%s" % dt)
        mqttc.publish("rpi/dht", "Temperature: %.1f C" % temp)
        mqttc.publish("rpi/dht", "Humidity:    %.1f %%" % humidity)
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
