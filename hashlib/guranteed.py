# guaranteed.py

import hashlib

print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_available))))
print('Available :\n{}\n'.format(', '.join(sorted(hashlib.algorithms_available))))
