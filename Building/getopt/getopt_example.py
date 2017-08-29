#!/usr/bin/env python3
# getopt_examply.py

import sys
import getopt

version = '1.0'
verbose = False
output_filename = 'default.out'

print('ARGV    :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'o:v',
        ['output=',
         'verbose',
         'version=',
        ])
except getopt.Getopterror as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS:    ', options)

for opt, args in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = args


print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_filename)
print('REMAINING :', remainder)

