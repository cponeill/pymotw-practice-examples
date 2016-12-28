#!/usr/bin/env python3

import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most Common')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))
