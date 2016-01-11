import paho.mqtt.publish as publish
publish.single("paho/test/single", "Hello", hostname=localhost)
msgs = [{'topic':"paho/test/multiple", 'payload':"Hello 1"}, ("paho/test/multiple", "Hello 2", 0, False)]
publish.multiple(msgs, hostname="localhost")
