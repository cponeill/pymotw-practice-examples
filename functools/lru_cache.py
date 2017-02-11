#! /usr/bin/env python3
# lru_cache.py

import functools


@functools.lru_cache()
def expensive(a, b): # Time Complexity -> O(n)
    print('expensive({}, {})'.format(a, b))
    return a * b


MAX = 2

print('First set of calls:')
for i in range(MAX): # Time Complexity -> O(n^2)
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecond set of calls:')
for i in range(MAX + 1): # Time Complexity -> O(n^2)
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThird set of calls:')
for i in range(MAX): # Time Complexity -> O(n^2)
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
