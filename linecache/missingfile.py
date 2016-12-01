#!/usr/bin/env python3

import linecache
from data import *

# Errors are hidden if linecache cannot find the file
no_such_file = linecache.getline(
    'this_file_does_not_exist.txt', 1,
)

print('NO FILE: {!r}'.format(no_such_file))
