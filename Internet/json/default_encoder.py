#!/usr/bin/env python3
# default_encoder.py

import json
import myobj


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        print('default(', repr(obj), ')')
        # Converts objects to a dictionary of their representation
        d = {
            '__class__': obj.__class__.__name__,
            '__module__': obj.__module__,
        }
        d.update(obj.__dict__)
        return d


obj = myobj.MyObj('internal data')
print(obj)
print(MyEncoder().encode(obj))
