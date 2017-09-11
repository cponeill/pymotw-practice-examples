#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pwd
import os

files = 'file.txt'
filename = 'fileowner.py'
stat_info = os.stat(filename)
owner = pwd.getpwuid(stat_info.st_uid).pw_name

print('{} is owned by {} ({})'.format(filename, stat_info, owner))
print('The name of the file is {}'.format(files))
