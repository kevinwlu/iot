import psutil
from time import sleep
for x in range(10):
    cpu = psutil.cpu_percent()
    print(cpu)
    sleep(1)
