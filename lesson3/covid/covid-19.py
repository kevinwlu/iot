# Mathematical modeling of infectious disease
import math
p = int(input('Enter population: '))
r = int(input('Enter infection rate: '))
s = int(input('Enter serial interval: '))
t = s*(math.log(2*p+1,r))
print('Time to infect:', t)
