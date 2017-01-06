#!/usr/bin/env python3

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<ellipsis.MyClass object at 0x...>]
    """
    return [obj]
