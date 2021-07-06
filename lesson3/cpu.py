# https://pypi.org/project/psutil/
import psutil

# Return the number of physical cores only
phy = psutil.cpu_count(logical=False)
print('The number of physical cores = ', phy)

# Return the number of logical CPUs in the system
log = psutil.cpu_count()
print('The number of logical CPUs = ', log)

# Returns a list of floats representing the utilization as a percentage for each CPU
print('The utilization per second as a percentage for each CPU')
for i in range(10):
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    print(cpu)
