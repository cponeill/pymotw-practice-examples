# echo_client.py

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
msg = b'This is the message to be sent'

try:

    # Send data
    print('sending {!r}'.format(msg))
    sent = sock.sendto(msg, server_address)

    # Receive message
    print('Waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    
    print('Closing socket')
    sock.close()
