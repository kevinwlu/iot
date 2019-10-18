import RPi.GPIO as GPIO
from urllib.request import urlopen, Request
from time import mktime, sleep
from datetime import datetime
from json import dumps
class Client (object):
    api_url = "http://api.carriots.com/streams"
    def __init__(self, api_key=None, client_type='json'):
        self.client_type = client_type
        self.api_key = api_key
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'Raspberry-Carriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type, 'Carriots.apikey': self.api_key}
        self.data = None
        self.response = None
    def send(self, data):
        self.data = dumps(data).encode()
        request = Request(Client.api_url, self.data, self.headers)
        self.response = urlopen(request)
        return self.response
def rc_time(pipin):
    measurement = 0
    GPIO.setup(pipin, GPIO.OUT)
    GPIO.output(pipin, GPIO.LOW)
    sleep(0.1)
    GPIO.setup(pipin, GPIO.IN)
    while GPIO.input(pipin) == GPIO.LOW:
        measurement += 1
    return measurement
def main():
    GPIO.setmode(GPIO.BCM)
    on = 1
    off = 2
    device = "YOUR DEVICE'S ID_DEVELOPER HERE"
    apikey = "YOUR APIKEY HERE"
    lights = off
    client_carriots = Client(apikey)
    while True:
        timestamp = int(mktime(datetime.utcnow().timetuple()))
        print(rc_time(24))
        if rc_time(24) > 600:
            new_lights = off
            print("Lights OFF")
        else:
            new_lights = on
            print("Lights ON")
        if lights is not new_lights:
            lights = new_lights
            data = {"protocol": "v2", "device": device, "at": timestamp, 
                    "data": dict(light=("ON" if new_lights is on
                    else "OFF"))}
            carriots_response = client_carriots.send(data)
            print(carriots_response.read())
if __name__ == '__main__':
    main()
