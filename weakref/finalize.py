#!/usr/bin/env python3
# finalize.py

import weakref


class ExpensiveObject:

    def __init__(self):
        print('(Deleting {})'.format(self))

def on_finalize(*args):
    print('on_finalize({!r})'.format(args))


obj = ExpensiveObject()
weakref.finalize(obj, on_finalize, 'extra argument')

del obj
