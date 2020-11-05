import paho.mqtt.client as mqtt
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
    client.subscribe("paho/test/multiple")
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
client.connect("localhost", 1883, 60)
client.loop_forever()
