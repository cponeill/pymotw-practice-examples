# matchcase.py

import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print('Pattern :', pattern)
print()

files = os.listdir('.')

for name in files:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatchcase(name, pattern)))
