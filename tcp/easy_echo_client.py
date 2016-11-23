# easy_echo_client.py

import socket
import sys

def get_constants(prefix):
    """Create a dictionary mapping socket module
       constants to their names.
    """
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print('Family   :', families[sock.family])
print('Type     :', types[sock.type])
print('Protocol :', protocols[sock.proto])

try:

    # Send data
    msg = b'This is some data that I am sending'
    print('Sending {!r}'.format(msg))
    sock.sendall(msg)

    amt_rec = 0
    amt_exp = len(msg)

    while amt_rec < amt_exp:
        data = sock.recv(16)
        amt_rec += len(data)
        print('Received {!r}'.format(data))

finally:
    print('Closing socket...')
    sock.close()
