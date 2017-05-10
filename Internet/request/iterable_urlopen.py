#!/usr/bin/env python3
# iterable_urlopen.py

from urllib import request

response = request.urlopen('http://localhost:8080')
for line in response:
    print(line.decode('utf-8').rstrip())
