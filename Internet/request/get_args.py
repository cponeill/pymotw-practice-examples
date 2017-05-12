#!/usr/bin/env python3
# get_args.py

from urllib import parse
from urllib import request

query_args = {'q': 'query_string', 'foo': 'bar'}
encoded_args = parse.urlencode(query_args)
print('ENCODED:', encoded_args)

url = 'http://localhost:8080/?' + encoded_args
print(request.urlopen(url).read().decode('utf-8'))
