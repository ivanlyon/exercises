'''
Compute difference in numbers from a fixed array of values representing the
counts for valid chess pieces.
'''

CORRECT = (1, 1, 2, 2, 2, 8)

###############################################################################

def get_difference(counts):
    '''Return difference in numbers from fixed array of 6 values.'''

    results = []
    for i in range(len(CORRECT)):
        results.append(str(CORRECT[i] - counts[i]))
    return ' '.join(results)

###############################################################################

if __name__ == '__main__':
    print(get_difference([int(i) for i in input().split()]))

###############################################################################
