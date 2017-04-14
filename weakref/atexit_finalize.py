#!/usr/bin/env python3
# atexit.py

import weakref
import sys

class ExpensiveObject:

    def __init__(self):
        print('(Deleting {}'.format(self))

def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
f = weakref.finalize(obj, on_finalize, 'extra argument')
f.atexit = bool(int(sys.argv[1]))
