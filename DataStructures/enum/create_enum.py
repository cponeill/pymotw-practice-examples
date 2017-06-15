#!/usr/bin/env python3
# create_enum.py

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commited = 2
    fix_released = 1


print('\nMember name: {}'.format(BugStatus.in_progress.name))
print('Member value: {}'.format(BugStatus.in_progress.value))
