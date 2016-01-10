import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)
outgoing = 'Hello from ROUTER 2'
print 'Sent "%s"' % outgoing
ser.write('%s\n' % outgoing)
