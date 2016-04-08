import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
x = np.random.random(10)
y = np.random.random(10)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'ro')
plt.plot([intercept,intercept+slope])
plt.show()
