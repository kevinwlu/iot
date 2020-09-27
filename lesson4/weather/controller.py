import time
import datetime
import board
import adafruit_dht
import sys
import requests
dhtDevice = adafruit_dht.DHT22(board.D24)
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
        hmd = dhtDevice.humidity
        tmp = dhtDevice.temperature
        if hmd is None or tmp is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
