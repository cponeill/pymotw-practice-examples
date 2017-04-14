#!/usr/bin/env python3
# valuedict.py

import gc
import weakref
from pprint import pprint

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObjec()'.format(self.name)

    def __del__(self):
        print('(Deleting {}'.format(self))


def demo(cache_factory):
    # Hold objects so any weak references
    # are not removed immediately.
    all_refs = {}
    # create the cache using the factory
    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print('    all_refs = ', end=' ')
    pprint(all_refs)
    print('\n   Before, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
        del value # decref

    # remove all references to objects except the cache
    print('\n  Cleanup:')
    del all_refs
    gc.collect()

    print('\n  After, cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
    print('  demo returning.')

demo(dict)
print()

demo(weakref.WeakValueDictionary)
