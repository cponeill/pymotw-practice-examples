# explicit_client.py

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port of server
# given by the caller
server_address = (sys.argv[1], 10000)
print('connection to on {} port {}'.format(*server_address))
sock.connection(server_address)

try:
    
    msg = b'This is a secret message. It will repeat.'
    print('sending {!r}'.fomat(msg))
    sock.sendall(msg)

    amt_rec = 0
    amt_exp = 0
    
    while amt_rec < amt_exp:
        data = sock.recv(16)
        amt_rec += len(data)
        print('received {!r}'.format(data))

finally:
    sock.close()
