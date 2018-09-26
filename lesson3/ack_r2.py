import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)
#ser = serial.Serial('/dev/ttyS0', 9600)
while True:
	try:
		incoming = ser.readline().strip()
		print('ROUTER_2 received "%s"' % incoming.decode())
	except KeyboardInterrupt:
		exit()
