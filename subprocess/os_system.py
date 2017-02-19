#! /usr/bin/env python3
# os_system.py
import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
