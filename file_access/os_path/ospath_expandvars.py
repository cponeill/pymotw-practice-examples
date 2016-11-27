# ospath_expandvars.py

import os.path
import os

os.environ['MY_VAR'] = 'VALUE'

print(os.path.expandvars('/path/to/$MYVAR'))
