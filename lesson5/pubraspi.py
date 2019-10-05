import time
import datetime
from system_info import get_temperature 
import psutil
import paho.mqtt.client as mqtt
mqttc = mqtt.Client()
mqttc.connect("mqtt.eclipse.org", 1883, 60)
mqttc.loop_start()
while True:
    try:  
        cpu = psutil.cpu_percent() 
        tmp = get_temperature()
        if cpu is None or tmp is None:
            time.sleep(2)
            continue
        now = datetime.datetime.now()
        dt = now.replace(microsecond=0)
        print(dt)
        print('Temperature: {0:0.1f} C'.format(tmp))
        print('CPU Usage:   {0:0.1f} %'.format(cpu))
        mqttc.publish("Raspberry Pi", "%s" % dt)
        mqttc.publish("Raspberry Pi", "Temperature: %.1f C" % tmp)
        mqttc.publish("Raspberry Pi", "CPU Usage:   %.1f %%" % cpu)
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
