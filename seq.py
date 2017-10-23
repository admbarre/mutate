#!/usr/local/bin/python3
import re, sys

def permute_single_base(mutation,sequence):
    permutations = []
    seq = list(sequence)
    for i,_ in enumerate(seq):
        copy_seq = seq[::]
        copy_seq[i] = mutation
        permutations.append(''.join(copy_seq))
    return permutations

def test(test, actual):
    print(f'Test: {test}')
    print(f'Actual: {actual}')
    print(f'Test == Actual: {test == actual}')

def main():
    # Commandline argument parsing
    if len(sys.argv) < 2:
        print('Usage: seq file')
        sys.exit()
    else:
        filename = sys.argv[1]

    # Load file
    with open(filename) as f:
        lines = f.readlines()
    sequence = ''.join(lines)

    # Testing
    permutations = permute_single_base('[gatc]', 'gaattc')
    # Sequence: GAATTC
    test_permutations  = [
            '[gatc]aattc',
            'g[gatc]attc',
            'ga[gatc]ttc',
            'gaa[gatc]tc',
            'gaat[gatc]c',
            'gaatt[gatc]']
    test(permutations, test_permutations)

    mutations = []
    for p in permutations:
        matches = re.findall(p,sequence)
        if matches:
            for match in matches:
                mutations.append(match)

    for i,m in enumerate(mutations):
        print(f'Mutation {i+1}: {m}')

if __name__ == '__main__':
    main()
