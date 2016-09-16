import serial

#ser = serial.Serial('/dev/cu.usbserial-AL0046V6', 9600)
ser = serial.Serial('/dev/ttyAMA0', 9600)
outgoing = 'Hello from COORDINATOR'
print('COORDINATOR sent "%s"' % outgoing)
ser.write('%s\n' % outgoing)
