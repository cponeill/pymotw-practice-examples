# ex_gethostname.py

import socket

HOSTS = [
    'blockshare-512mb-nyc3-01',
    'pymotw.com',
    'www.bitcoin.org',
    'www.python.org.',
    'nosuchname'
]

for host in HOSTS:
    print(host)
    try:
        name, alias, addresses = socket.gethostbyname_ex(host)
        print('   HOSTNAME:', name)
        print('    ALIASES:', alias)
        print('  ADDRESSES:', addresses)
    except socket.error as msg:
        print('ERROR:', msg)
    print()
