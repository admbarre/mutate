#!/usr/local/bin/python3
import re, sys

if len(sys.argv) < 2:
    print('Usage: seq file')
    sys.exit()
else:
    filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()
sequence = ''.join(lines)
print(f'Sequence: {sequence}')

def permute_single_base(mutation,sequence):
    pass

# Sequence: GAATTC
permutations  = [
        '[gatc]aattc',
        'g[gatc]attc',
        'ga[gatc]ttc',
        'gaa[gatc]tc',
        'gaat[gatc]c',
        'gaatt[gatc]']
mutations = []
for p in permutations:
    matches = re.findall(p,sequence)
    if matches:
        for match in matches:
            mutations.append(match)

for i,m in enumerate(mutations):
    print(f'Mutation {i+1}: {m}')
