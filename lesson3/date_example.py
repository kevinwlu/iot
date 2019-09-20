from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
midterm = date(2019, 10, 15)
final = date(2019, 12, 2)
timediff = midterm - now
print('{:d} days to midterm'.format(timediff.days))
timediff = final - now
print('{:d} days to final'.format(timediff.days))
