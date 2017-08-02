#!/usr/bin/env python3
# depth.py

from pprint import pprint
from data import data

for width in [80, 5]:
    print('WIDTH=', width)
    pprint(data, width=width)
    print()
