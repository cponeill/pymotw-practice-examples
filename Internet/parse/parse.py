#!/usr/bin/env python3
# parse.py

from urllib.parse import urlparse

url = 'https://www.request402.com/domain_ip?url=google.com'
parsed = urlparse(url)
print(parsed)
print('scheme:', parsed.scheme)
print('network location:', parsed.netloc)
print('path:', parsed.path)
print('query:', parsed.query)
