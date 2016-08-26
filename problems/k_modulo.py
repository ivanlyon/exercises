'''
Count number of unique modulus values achieved from modulo 42.
'''

import sys
from collections import defaultdict

if __name__ == '__main__':
    moduli = defaultdict(int)
    for number in sys.stdin:
        moduli[int(number) % 42] += 1

    print(len(moduli))
