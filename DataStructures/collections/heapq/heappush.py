#!/usr/bin/env python3
# heappush.py

import heapq
from showtree import show_tree
from data import data

heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)
