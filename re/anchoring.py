# anchoring.py

from test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation',
    [(r'^\w+', 'word at the start of a string'),
     (r'\A\w+', 'word at the start of a string'),
     (r'\w+\S*$', 'word near the end of a string'),
     (r'\w+\S*\Z', 'word near the end of a string'),
     (r'\w*t\w*', 'word containing the letter t'),
     (r'\bt\w+', 'letter t at the start of a word'),
     (r'\w+t\b', 'letter t at the end of a word'),
     (r'\Bt\B', 'letter t, not start or end of a word')],
)
