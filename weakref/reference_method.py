#!/usr/bin/env python3
# reference_method.py

import gc
import weakref


class ExpensiveObject:

    def __init__(self):
        print('(Deleting {}'.format(self))

    def do_finalize(self):
        print('do_finalize')


obj = ExpensiveObject()
obj_id = id(obj)

f = weakref.finalize(obj, obj.do_finalize)
f.atexit = False

for o in gc.get_objects():
    if id(o) == obj_id:
        print('found uncollected object in gc')
