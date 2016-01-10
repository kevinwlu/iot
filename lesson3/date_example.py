from datetime import date
now = date.today()
print 'Date: ' + now.isoformat()
print 'Date: ' + now.strftime('%m-%d-%y')
print 'Day of Week: ' + now.strftime('%A')
print 'Month: ' + now.strftime('%B')
print 'Year: ' + now.strftime('%Y')
newyear = date(2016, 2, 8)
timediff = newyear - now
print '%d days to Lunar New Year' %(timediff.days)

