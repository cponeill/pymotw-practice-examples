#!/usr/bin/env python3
# comparison.py

import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix
desire_state = BugStatus.fix_released

print('Equality:',
      actual_state == desire_state,
      actual_state == BugStatus.wont_fix)
print('Identity:',
      actual_state is desire_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))
