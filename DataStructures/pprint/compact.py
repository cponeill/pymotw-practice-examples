#!/usr/bin/env python3
# compact.py

from pprint import pprint
from data import data


print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)
