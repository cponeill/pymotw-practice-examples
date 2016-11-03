# shorten.py

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Original:\n')
print(original)

shortened_text = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened_text, width=50)

print('\nShortened:\n')
print(shortened_wrapped)
