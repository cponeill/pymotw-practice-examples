#!/usr/bin/env python3

import collections

def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

    >>> grouped = group_by_length(['python', 'module', 'of',
    ... 'the', 'week'])

    >>> grouped = group_by_length([ 'python', 'module', 'of',
    ... 'the', 'week' ])
    >>> grouped == { 2:set(['of']),
    ...              3:set(['the']),
    ...              4:set(['week']),
    ...              6:set(['python', 'module']),
    ...              }
    True

    """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d
