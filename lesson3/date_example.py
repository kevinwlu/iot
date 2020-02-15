from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
first = date(2020, 1, 21)
last = date(2020, 5, 6)
timediff = now - first
print('{:d} days since the first day of classes'.format(timediff.days))
timediff = last - now
print('{:d} days to the last day of classes'.format(timediff.days))
