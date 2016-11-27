# ospath_splitext.py

import os

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.'
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.splitext(path)))
