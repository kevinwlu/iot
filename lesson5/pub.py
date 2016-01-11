import paho.mqtt.publish as publish
publish.single("paho/test", "Hello", hostname="localhost")
