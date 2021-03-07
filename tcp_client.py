#!/usr/bin/env python3

import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 50000        # The port used by the server

#creating the socket with address type as ipv4(AF_INET)
#and tcp (SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server using host and port
sock.connect((HOST, PORT))
# send data after connecting
sock.sendall(b'Hello, world')
# receive the data from server which is echoed sent data
data = sock.recv(1024)

print('Received', repr(data))
#close the socket connection
sock.close()
