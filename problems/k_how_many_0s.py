'''
Compute difference in numbers from a fixed array of values representing the
counts for valid chess pieces.
'''

import math
import sys

###############################################################################

def zeroes(number):
    '''Compute number of zero digits in range of 0 to some number.'''
    if number < 0: return 0
    if number == 0: return 1

    result = 1
    for exponent in range(int(math.log10(number))):
        digit_mask = 10**exponent

        lhs = number // (digit_mask * 10)
        result += lhs * digit_mask

        if (number // digit_mask) % 10 == 0:
            result += number % digit_mask + 1 - digit_mask

    return result

###############################################################################

def difference(lo, hi):
    '''Compute difference of two spanning sums.  Here for TDD.'''

    return zeroes(hi) - zeroes(lo - 1)

###############################################################################

if __name__ == '__main__':
    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, then all below is stderr.      |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    while True:
        lo, hi = [int(i) for i in input().split()]
        if lo < 0:
            break
        print('# of zeroes between {} and {} = '.format(lo, hi),
              end='',
              flush=True,
              file=sys.stderr)
        print(str(difference(lo, hi)))

###############################################################################
