#!/usr/bin/env python3
# a_post_request.py

from urllib import parse
from urllib import request

query_args = {'q': 'query_args', 'foo': 'bar'}

r = request.Request(
    url='http://localhost:8080/',
    data=parse.urlencode(query_args).encode('utf-8'),
)
print('Request Method: ', r.get_method())
r.add_header(
    'User-Agent',
    'Blockshare Technologies, LLC. (https://blockshare.io)',
)

print()
print('OUTGOING DATA:')
print(r.data)

print()
print('SERVER RESPONSE:')
print(request.urlopen(r).read().decode('utf-8'))
