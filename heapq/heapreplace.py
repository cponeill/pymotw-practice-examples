#!/usr/bin/env python3

import heapq
from showtree import show_tree
from heapdata import data

heapq.heapify(data)
print('start:')
show_tree(data)

lst = [0, 13]

for n in lst:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}'.format(smallest, n))
    show_tree(data)
