# Mathematical modeling of infectious disease
import math
import sys
p = int(sys.argv[1])
r = int(sys.argv[2])
s = int(sys.argv[3])
print('Population      =', p)
print('Infection rate  =', r)
print('Serial interval =', s)
t = s*(math.log(2*p+1,r))
print('Time to infect  =', t)
