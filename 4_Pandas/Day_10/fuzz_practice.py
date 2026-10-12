# fuzz : fuzz usually refers to fuzzy string matching — comparing two strings to determine how similar they are, even when they aren't exactly equal.

import pandas as pd
from thefuzz import fuzz

one = 'A'
two = 'A'

print(fuzz.partial_ratio(one,two))