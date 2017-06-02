#!/usr/bin/env python3
# indent.py

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))

print('Normal: ', json.dumps(data, sort_keys=True))
print('Indent: ', json.dumps(data, sort_keys=True, indent=2))
