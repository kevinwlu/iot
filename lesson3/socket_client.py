# Echo client program
import sys
import socket
HOST = sys.argv[1]        # The remote host IP address
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world'.encode())
data = s.recv(1024).decode()
s.close()
print('Received', repr(data))
