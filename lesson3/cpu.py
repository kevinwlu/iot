import psutil
for x = range(10)
    cpu = psutil.cpu_percent()
    print(cpu)
    sleep(1)
