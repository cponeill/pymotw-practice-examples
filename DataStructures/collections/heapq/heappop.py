#!/usr/bin/env python3
# heappop.py

import heapq
from showtree import show_tree
from data import data

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)

for i in range(5):
    smallest = heapq.heappop(data)
    print('pop    {:>3}'.format(smallest))
    show_tree(data)
