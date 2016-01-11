import paho.mqtt.publish as publish
msgs = [{'topic':"paho/test/multiple", 'payload':"multiple 1"},
    ("paho/test/multiple", "multiple 2", 0, False)]
publish.multiple(msgs, hostname="localhost")
