#!/usr/bin/env python3
# heapify.py

import heapq
from showtree import show_tree
from data import data

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
