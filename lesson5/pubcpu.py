import time
import datetime
import psutil
import paho.mqtt.client as mqtt
#mqttc = mqtt.Client()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
#mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
#mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.loop_start()
while True:
    try:  
        cpu = psutil.cpu_percent() 
        if cpu is None:
            time.sleep(2)
            continue
        now = datetime.datetime.now()
        dt = now.replace(microsecond=0)
        print(dt)
        print('CPU Usage:   {0:0.1f} %'.format(cpu))
        mqttc.publish("MyCPU", "%s" % dt)
        mqttc.publish("MyCPU", "CPU Usage:   %.1f %%" % cpu)
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
