#!/usr/bin/env python3

import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1', a)

# Write the array of numbers to a temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

# Read the raw data
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read the input into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)
