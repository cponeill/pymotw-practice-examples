#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import queue

q = queue.Queue()

for i in range(0, 11):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print()
