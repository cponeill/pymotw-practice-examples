#!/usr/bin/env python3
# sequence.py

import array
import pprint

a = array.array('i', range(3))
print('Initial :', a)

a.extend(range(3))
print('Extended:', a[2:5])

print('Slice   :', a[2:5])

print('Iterator')
print(list(enumerate(a)))
