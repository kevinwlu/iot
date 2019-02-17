from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
midterm = date(2019, 3, 11)
final = date(2019, 5, 6)
timediff = midterm - now
print('{:d} days to Midterm Exam'.format(timediff.days))
timediff = final - now
print('{:d} days to Final Exam'.format(timediff.days))
