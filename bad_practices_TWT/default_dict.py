# Using base Python library
counts = {}
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for key in numbers:
    if key not in counts:
        counts[key] = 0
    counts[key] += 1

print(counts)

# Using default dict
from collections import defaultdict

counts = defaultdict(lambda: 0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for key in numbers:
    counts[key] += 1

print(counts)


# Using lists with dicts

# Base Python library
d = {}

if 'list' not in d:
    d['list'] = []

d['list'].append(3)

print(d)

# Using default dict
d = {}

d.setdefault('list', []).append(3)

print(d)