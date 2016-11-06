# escape_codes.py

from test_patterns import test_patterns

test_patterns(
    'A prime 1 example',
    [(r'\d+', 'sequence of digits'),
     (r'\D+', 'sequence of non-digits'),
     (r'\s+', 'sequence of white space'),
     (r'\S+', 'sequence of non white space'),
     (r'\w+', 'alphanumeric characters'),
     (r'\W+', 'nonalphanumeric')],
)
