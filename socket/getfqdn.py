# getfqdn.py

import socket

for host in ['blockshare', 'pymotw.org']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))
