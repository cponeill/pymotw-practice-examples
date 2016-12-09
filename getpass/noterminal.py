#!/usr/bin/env python3

import getpass
import sys

if sys.stdin.isatty():
    pwd = getpass.getpass('Using getpass: ')
else:
    print('Using readline')
    pwd = sys.stdin.readline().rstrip()

print('Read: ', pwd)
