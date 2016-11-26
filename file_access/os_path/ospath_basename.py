# ospath_basename.py

import os

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    ',',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))
