#!/usr/bin/env python3
# new_child.py

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 Before:', m1)
print('m1 After :', m2)

m2['c'] = 'E'

print('m1 after:', m1)
print('m2 after:', m2)
