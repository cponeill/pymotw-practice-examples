#!/usr/bin/env python3

import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print('You entered ', p)
