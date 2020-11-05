import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    """
    Callback invoked when the client

    Args:
        client: (todo): write your description
        userdata: (str): write your description
        flags: (str): write your description
        rc: (str): write your description
    """
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/broker/publish/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    """
    Callback invoked when a message is received

    Args:
        client: (todo): write your description
        userdata: (str): write your description
        msg: (str): write your description
    """
    print(msg.topic+" "+str(msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
