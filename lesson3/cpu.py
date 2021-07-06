import psutil
for i in range(10):
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    print(cpu)
