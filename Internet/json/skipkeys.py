#!/usr/bin/env python3
# shipkeys.p

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

print('First Attempt')
try:
    print(json.dumps(data))
except TypeError as e:
    print('ERROR:', e)

print()
print('Second Attempt')
print(json.dumps(data, skipkeys=True))
