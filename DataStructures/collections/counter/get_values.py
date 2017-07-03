#!/usr/bin/env python3
# get_values.py

import collections

c = collections.Counter('abcdaab')
letters = 'abcde'

for letter in letters:
    print('{} : {}'.format(letter, c[letter]))
