from datetime import date
from astral.geocoder import database, lookup
from astral.sun import sun
from astral import LocationInfo
l = LocationInfo('Xidian', 'China', 'Asia/Shanghai', 34.12250, 108.84029)
s = sun(l.observer, date=date.today(), tzinfo=l.timezone)
print('Dawn:    %s' % str(s['dawn']))
print('Sunrise: %s' % str(s['sunrise']))
print('Noon:    %s' % str(s['noon']))
print('Sunset:  %s' % str(s['sunset']))
print('Dusk:    %s' % str(s['dusk']))
