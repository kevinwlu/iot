import time
import datetime
import sys
import requests
import psutil
from system_info import get_temperature
def runController():
    """
    Runs a new run.

    Args:
    """
    now = datetime.datetime.now()
    dt = now.replace(microsecond=0)
    print(dt)
    print('Temperature: {0:0.1f} C'.format(tmp))
    print('CPU Usage:   {0:0.1f} %'.format(cpu))
    setDtState(dt)
    setTmpState(tmp)
    setCpuState(cpu)
def setDtState(val):
    """
    Sets the state of the led.

    Args:
        val: (float): write your description
    """
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/dt/1/', data=values, auth=('pi', 'raspberry'))
def setTmpState(val):
    """
    Set the tmp tmp state.

    Args:
        val: (int): write your description
    """
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/tmp/1/', data=values, auth=('pi', 'raspberry'))
def setCpuState(val):
    """
    Sets the cpu connection.

    Args:
        val: (int): write your description
    """
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/cpu/1/', data=values, auth=('pi', 'raspberry'))
while True:
    try:
        tmp = get_temperature()
        cpu = psutil.cpu_percent()
        if cpu is None or tmp is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
