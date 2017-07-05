#!/usr/bin/env python3
# update.py

import collections

c = collections.Counter()
print('Initial  :', c)

c.update('abcdaab')
print('Sequence :', c)

c.update({'a': 1, 'd': 5})
print('Dict     :', c)
