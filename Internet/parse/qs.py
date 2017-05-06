#!/usr/bin/env python3
# qs.py

from urllib.parse import parse_qs, parse_qsl

encoded = 'foo=foo1&foo=foo2'

print('parse qs :', parse_qs(encoded))
print('parse qsl:', parse_qsl(encoded))
