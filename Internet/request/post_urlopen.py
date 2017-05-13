#!/usr/bin/env python3
# post_urlopen.py

from urllib import parse
from urllib import request


query_args = {'q': 'query_args', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args).encode('utf-8')
url = 'http://localhost:8080/'
print(request.urlopen(url, encoded_args).read().decode('utf-8'))
