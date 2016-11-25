# echo_client.py

import socket
import sys
import os

# Creat a UDS socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect te socket to the port where the server is listening
server_addres = './uds_socket'
print('connection to {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as error:
    print(error)
    sys.exit[1]
