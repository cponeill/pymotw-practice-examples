#!/usr/bin/env python3
import tempfile

print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())


tempfile.tempdir = '/I/changed/this/path'
print('gettempdir():', tempfile.gettempdir())
