from datetime import date, timedelta
from astral import Astral
now = date.today()
a = Astral()
for i in range(30):
    day = now + timedelta(days=i)
    moon = a.moon_phase(day)
    print(day.isoformat() + ' Moon Phase: %d' % moon)
