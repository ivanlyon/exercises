'''
Count negative numbers in a list.

Status: Accepted
'''
import sys

###############################################################################

def count_negatives(numbers):
    '''Count of numbers less than zero.'''

    result = 0
    for n in numbers:
        if n < 0:
            result += 1

    return result

###############################################################################

if __name__ == '__main__':
    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, then all below is stderr.      |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    numbers = int(input())
    number_list = [int(i) for i in input().split()]

    print('Count of negative numbers in {} = '.format(str(number_list)),
          end='',
          flush=True,
          file=sys.stderr)

    print(str(count_negatives(number_list)))

###############################################################################
