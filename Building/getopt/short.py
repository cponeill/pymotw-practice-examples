#!/usr/bin/env python3
# short.py

import getopt

opts, args = getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c')

for opt in opts:
    print(opt)
