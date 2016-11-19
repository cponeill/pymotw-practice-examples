# gethostbyaddr.py

import socket

hostname, aliases, addresses = socket.gethostbyaddr('127.0.0.1')

print('  HOSTNAME:', hostname)
print('   ALIASES:', aliases)
print(' ADDRESSES:', addresses)
