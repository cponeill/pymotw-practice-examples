#!/usr/bin/env python3

import getpass

try:
    p = getpass.getpass()
except Exception as err:
    print('There was an error,', err)
else:
    print('Password:', p)
