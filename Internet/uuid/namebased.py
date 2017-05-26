#!/usr/bin/env python3
# namebased.py

import uuid

hostnames = ['https://www.request402.com', 'https://www.request402.com/ip']

for name in hostnames:
    print(name)
    print('  MD5    :', uuid.uuid3(uuid.NAMESPACE_DNS, name))
    print('  SHA-1  :', uuid.uuid5(uuid.NAMESPACE_DNS, name))
    print()
