#!/usr/bin/env python3
# request_header.py

from urllib import request

r = request.Request('http://localhost:8080/')
r.add_header(
    'User-Agent',
    'Blockshare Technologies, LLC (https://blockshare.io)',
)

response = request.urlopen(r)
data = response.read().decode('utf-8')
print(data)
