from datetime import date
now = date.today()
print('Date: ' + now.isoformat())
print('Date: ' + now.strftime('%m-%d-%y'))
print('Day of Week: ' + now.strftime('%A'))
print('Month: ' + now.strftime('%B'))
print('Year: ' + now.strftime('%Y'))
midterm = date(2018, 02, 26)
final = date(2018, 04, 30)
timediff = midterm - now
print('{:d} days to Midterm Exam'.format(timediff.days))
timediff = final - now
print('{:d} days to Final Exam'.format(timediff.days))
