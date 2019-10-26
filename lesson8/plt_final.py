import matplotlib.pyplot as plt
from pandas import *
from scipy import stats

data = read_csv('rpidata1.csv')
x = data['CPU Usage %']
y = data['Temperature C']

# Time series
plt.plot(y, 'r', lw=2, label='Temperature C')
plt.plot(x, 'b', lw=2, label='CPU Usage %')
plt.xticks([209,452,703,957],['21:00','21:30','22:00','22:30'])
plt.xlabel('Time')
plt.legend(loc='lower center')
plt.title('Iotu 2017-04-28')

# Histogram of CPU usage
plt.figure()
num_bins = 35
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage %')
plt.ylabel('Probability')
plt.title('Iotu 2017-04-28')

# Histogram of temperature
plt.figure()
num_bins = 30
n, bins, patches = plt.hist(y, num_bins, density=1, facecolor='red', alpha=0.5)
plt.xlabel('Temperature C')
plt.ylabel('Probability')
plt.title('Iotu 2017-04-28')

# Horizontal box plot of CPU usage
plt.figure()
plt.boxplot(x, 0, '+', 0)
plt.xlabel('CPU Usage %')
plt.title('Iotu 2017-04-28')

# Vertical box plot of temperature
plt.figure()
plt.boxplot(y, 0, '+')
plt.ylabel('Temperature C')
plt.title('Iotu 2017-04-28')

# Scatter diagram with a linear regression line
plt.figure()
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.xlabel('CPU Usage %')
plt.ylabel('Temperature C')
plt.plot(x, y, 'bo')
l = [slope * i + intercept for i in x]
plt.plot(x, l, 'r', lw=2)
plt.title('Iotu 2017-04-28')

plt.show()
