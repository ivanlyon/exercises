'''
Compute number of digits in a factorial.

Status: Accepted
'''
import sys
import math

LOG10_SUMMATION = [1, 1]
for n in range(2, 1000001):
    LOG10_SUMMATION += [math.log10(n) + LOG10_SUMMATION[-1]]

###############################################################################

def counted(number):
    '''Return number of digits in (number)!'''

    return int(LOG10_SUMMATION[number])

###############################################################################

if __name__ == '__main__':
    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, then all below is stderr.      |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    for testcase in sys.stdin:
        print('The # of digits in {}! = '.format(testcase),
              end='',
              flush=True,
              file=sys.stderr)

        print(str(counted(int(testcase))))

###############################################################################
