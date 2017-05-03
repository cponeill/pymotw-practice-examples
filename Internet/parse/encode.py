#!/usr/bin/env python3
# encode.py

from urllib.parse import urlencode, urljoin

query_args = {
    'q': 'query_strings',
    'foo': 'bar',
}

encoded_args = urlencode(query_args)
print('ENCODED: ', encoded_args)


req_args = {
    'foo': ['foo1', 'foo2']
}

print('SINGLE   :', urlencode(req_args))
print('SEQUENCE :', urlencode(req_args, doseq=True))
