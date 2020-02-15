from datetime import date, timedelta
from astral import moon
now = date.today()
for i in range(30):
    day = now + timedelta(days=i)
    moon_phase = moon.phase(day)
    print(day.isoformat() + ' Moon Phase: %d' % moon_phase)
