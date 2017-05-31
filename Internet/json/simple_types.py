#!/usr/bin/env python3
# simple_types.py

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA', repr(data))

data_string = json.dumps(data)
print('DATA', data_string)
