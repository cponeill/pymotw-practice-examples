#!/usr/bin/env python3

import heapq
from showtree import show_tree
from heapdata import data

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
