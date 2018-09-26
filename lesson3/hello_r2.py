import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyS0', 9600)
outgoing = b'Hello from ROUTER 2'
print('Sent "%s"' % outgoing.decode())
ser.write('%s\n'.encode() % outgoing)
