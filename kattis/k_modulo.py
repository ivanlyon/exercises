'''
Count number of unique modulus values achieved from modulo 42.

Status: Accepted
'''

import sys
from collections import defaultdict

###############################################################################

def partition_dict(inputs):
    '''Create a dictionary counting # of times an index has been computed'''
    moduli = defaultdict(int)
    for number in inputs:
        moduli[number % 42] += 1

    return moduli

###############################################################################

if __name__ == '__main__':
    inputs = []
    for i in sys.stdin:
        inputs.append(int(i))
    print(len(partition_dict(inputs)))

###############################################################################
