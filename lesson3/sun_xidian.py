from datetime import date
from astral.geocoder import database, lookup
from astral.sun import sun
from astral import LocationInfo
l = LocationInfo(('Xidian', 'China',  34.12250,108.84029, 'Asia/Shanghai', 0))
 # Record the location of Xichong, pay attention to the longitude first and then the latitude
s = l.sun(date=date.today(),local=True)
print('Dawn:    %s' % str(s['dawn']))
print('Sunrise: %s' % str(s['sunrise']))
print('Noon:    %s' % str(s['noon']))
print('Sunset:  %s' % str(s['sunset']))
print('Dusk:    %s' % str(s['dusk']))
