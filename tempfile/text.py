#!/usr/bin/env python3

import tempfile

with tempfile.TemporaryFile(mode='w+t') as f:
    f.write(['first\n', 'second\n'])

    f.seek(0):
    for line in f:
        print(line.rstrip())
