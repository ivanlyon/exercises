'''
Compute catalan number.

Status: Accepted
'''

import math
import sys

###############################################################################

def catalan(number):
    '''Compute catalan number.'''

    fact_n = math.factorial(number)
    fact_n_plus_1 = fact_n * (number + 1)

    return math.factorial(2 * number) // (fact_n * fact_n_plus_1)

###############################################################################

if __name__ == '__main__':
    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, then all below is stderr.      |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    for testcase in range(int(input())):
        number = int(input())
        print('Catalan({}) = '.format(number),
              end='',
              flush=True,
              file=sys.stderr)
        print(catalan(number))

###############################################################################
