import time
import datetime
import sys
import requests
import psutil
def runController():
    now = datetime.datetime.now()
    dt = now.replace(microsecond=0)
    print(dt)
    print('CPU Usage:        {0:0.1f}%'.format(cpu))
    print('Memory Available: {0:0.1f} GB'.format(mem))
    setDtState(dt)
    setMemState(mem)
    setCpuState(cpu)
def setDtState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/dt/1/', data=values, auth=('admin', 'admin'))
def setMemState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/mem/1/', data=values, auth=('admin', 'admin'))
def setCpuState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/cpu/1/', data=values, auth=('admin', 'admin'))
while True:
    try:
        memory = psutil.virtual_memory()
        mem = memory.available/(1024**3)
        cpu = psutil.cpu_percent()
        if cpu is None or mem is None:
            time.sleep(2)
            continue
        runController()
        time.sleep(10)
    except KeyboardInterrupt:
        exit()
