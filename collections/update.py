#!/usr/bin/env python3

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'd': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After: {}'.format(m['c']))
