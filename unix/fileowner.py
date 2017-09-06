#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pwd
import os

filename = 'fileowner.py'
stat_info = os.stat(filename)
owner = pwd.getpwuid(stat_info.st_uid).pw_name

print('{} is owned by {} ({})'.format(filename, stat_info, owner))
