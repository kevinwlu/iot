import psutil
# Return the number of logical CPUs in the system
log = psutil.cpu_count()
print('The number of logical CPUs = ', log)
# Return the number of physical cores only
phy = psutil.cpu_count(logical=False)
print('The number of physical cores = ', phy)
# Return hardware temperatures
tmp = psutil.sensors_temperatures()
print('Hardware emperatures in degrees Celsius')
print(tmp)
# Returns a list of floats representing the utilization as a percentage for each CPU
print('The utilization as a percentage for each CPU')
for i in range(10):
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    print(cpu)
