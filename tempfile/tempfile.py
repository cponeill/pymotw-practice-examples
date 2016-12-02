#!/usr/env/bin python3

import os
import tempfile

print('Building a file name with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpid())
with open(filename, 'w') as temp:
    print('TEMP:')
    print('   {!r}'.format(temp))
    print('temp.name')
    print('   {!r}'.format(temp.name))


# Clean up the temporary file yourself.
os.remove(filename)

print()
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))
