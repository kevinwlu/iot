import time
import datetime
import Adafruit_DHT
import sys
import requests
DHT_TYPE = Adafruit_DHT.DHT22
DHT_PIN  = 24
def runController():
    now = datetime.datetime.now()
    dt = now.replace(microsecond=0)
    print(dt)
    print('Temperature: {0:0.1f} C'.format(tmp))
    print('Humidity:    {0:0.1f} %'.format(hmd))
    setDtState(dt)
    setTmpState(tmp)
    setHmdState(hmd)
def setDtState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/dt/1/', data=values, auth=('pi', 'raspberry'))
def setTmpState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/tmp/1/', data=values, auth=('pi', 'raspberry'))
def setHmdState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/hmd/1/', data=values, auth=('pi', 'raspberry'))
while True:
    try:
        hmd, tmp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
        if hmd is None or tmp is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
