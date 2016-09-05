from datetime import date
now = date.today()
print 'Date: ' + now.isoformat()
print 'Date: ' + now.strftime('%m-%d-%y')
print 'Day of Week: ' + now.strftime('%A')
print 'Month: ' + now.strftime('%B')
print 'Year: ' + now.strftime('%Y')
final = date(2016, 12, 12)
timediff = final - now
print '%d days to final' %(timediff.days)
