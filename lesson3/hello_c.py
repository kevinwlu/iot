import serial

#ser = serial.Serial('/dev/cu.usbserial-AL0046V6', 9600)
ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyS0', 9600)
outgoing = b'Hello from COORDINATOR'
print('COORDINATOR sent "%s"' % outgoing.decode())
ser.write('%s\n'.encode() % outgoing)
