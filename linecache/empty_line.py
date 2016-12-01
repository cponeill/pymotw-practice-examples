#!/usr/bin/env python3

import linecache
from data import *

filename = make_tempfile()

# Blank lines include the newline
print('BLANK : {!r}'.format(linecache.getline(filename, 8)))

cleanup(filename)
