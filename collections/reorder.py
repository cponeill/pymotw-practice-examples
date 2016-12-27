#!/usr/bin/env python3

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'd': 'D'}

m = collections.ChainMap(a, b)

print(m.maps)
print('c = {}\n'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}\n'.format(m.maps))
