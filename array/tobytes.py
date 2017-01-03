#!/usr/bin/env python3

import array
import binascii

a = array.array('i', range(5))
print('A1:', a)

as_bytes = a.tobytes()
print('Bytes:', binascii.hexlify(a))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)
