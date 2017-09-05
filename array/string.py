#!/usr/bin/env python3

import array
import binascii

s = b'This is the array'
a = array.array('b', s)
b = b'another array.'

print('As byte string:', s)
print('As array      :', a)
print(b)
print('As hex        :', binascii.hexlify(a))
print('More hex      :', binascii.hexlify(b))
