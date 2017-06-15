#!/usr/bin/env python3
# iterate.py

import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commited = 2
    fix_released = 1

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

