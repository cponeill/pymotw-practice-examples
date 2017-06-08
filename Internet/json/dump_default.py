#!/usr/bin/env python3
# dump_default.py

import json
import myobj

obj = myobj.MyObj('instance value goes here')

print('First Attempt')
try:
    print(json.dumps(obj))
except TypeError as err:
    print('ERROR:', err)

def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    # Convert objects to a dictionary of their representation.
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print()
print('With Default')
print(json.dumps(obj, default=convert_to_builtin_type))
