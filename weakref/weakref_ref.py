#!/usr/bin/env python3
# weakref_ref.py

import weakref

	
class ExpensiveObject:

    def __init__(self):
        print('(Deleting {})'.format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
