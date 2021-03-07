#!/usr/bin/env python3

import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on 

#creating the socket with address type as ipv4(AF_INET)
#and tcp (SOCK_STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
#waiting for the client to establish the connection
sock.listen()
#accept the connection from client once client requests
conn, addr = sock.accept()
with conn:
    print('Connection request accepted from', addr)
    while True:
        #receive the data from client using conn.recv and max of 1024 bytes
        data = conn.recv(1024)
        if not data:
            break
        #echo the data received
        #add "server:" to the received data
        conn.sendall(b"server:" + data)
