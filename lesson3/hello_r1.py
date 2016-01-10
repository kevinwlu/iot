import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)
outgoing = 'Hello from ROUTER 1'
print 'Sent "%s"' % outgoing
ser.write('%s\n' % outgoing)
