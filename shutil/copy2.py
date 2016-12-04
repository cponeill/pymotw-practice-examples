#!/usr/bin/env python3

import os
import shutil
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print('\tMode    :', oct(stat_info.st_mode))
    print('\tCreated :', time.ctime(stat_info.st_ctime))
    print('\tAccessed:', time.ctime(stat_info.st_atime))
    print('\tModified:', time.ctime(stat_info.st_mtime))


os.mkdir('example')
print('SOURCE:')
show_file_info('shutil_copy2.py')

shutil.copy2('shutil_copy2.py', 'example')

print('DEST:')
show_file_info('example/shutil_copy2.py')
