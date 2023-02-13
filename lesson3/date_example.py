from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
first = date(2023, 1, 18)
last = date(2023, 5, 4)
timediff = now - first
print('{:d} days after the first day of classes'.format(timediff.days))
timediff = last - now
print('{:d} days before the last day of classes'.format(timediff.days))
