# compile.py

import re

# pre-compile the patterns in a list.
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]

text = 'Does this text match the pattern?.'

print('Text: {!r}\n'.format(text))

# loop through 'regexes' list to find the pattern.
for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')
