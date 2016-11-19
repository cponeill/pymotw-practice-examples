# gethostname.py

import socket


HOSTS= [
    'blockshare-512mb-nyc3-01',
    'pymotw.com',
    'www.python.org',
    'www.request402.com',
    'nosuchname'
]

for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as error:
        print('{} : {}'.format(host, error))
