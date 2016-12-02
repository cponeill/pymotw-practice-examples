#!/usr/bin/env python3

import os
import socket

with tempfile.TemporaryFile() as temp:
    temp.write(b'some data')
    
    temp.seek(0)
    print(temp.read())
