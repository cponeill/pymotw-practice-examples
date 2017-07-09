#!/usr/bin/env python3
#! file.py

import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1', a)

# Write the array of numbers to a temporary file
output = tempfile.NamedTemporary()
a.tofile(output.file)
output.flush()

with open(output.name, 'rb') as f:
    raw_data = intput.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read the data into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)
