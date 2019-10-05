import time
import datetime
import Adafruit_DHT
import paho.mqtt.client as mqtt
DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN  = 24
mqttc = mqtt.Client()
mqttc.connect("mqtt.eclipse.org", 1883, 60)
mqttc.loop_start()
while True:
    try:  
        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
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
