# subdir.py

import glob

print('Named explicitly')
for name in sorted(glob.glob('dir/subdir/*')):
    print(name)

print('Named with wildcard')
for name in sorted(glob.glob('dir/*/*')):
    print(name)
