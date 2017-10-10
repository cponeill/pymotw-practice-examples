#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import queue

q = queue.LifoQueue()

for i in range(5):
  q.put(i)

while not q.empty():
  print(q.get(), end=' ')
print()
