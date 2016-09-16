import serial

#ser = serial.Serial('/dev/cu.usbserial-AL0046V6', 9600)
ser = serial.Serial('/dev/ttyAMA0', 9600)
while True:
	try:
		incoming = ser.readline().strip()
		print('COORDINATOR received "%s"' % incoming)
	except KeyboardInterrupt:
		exit()
