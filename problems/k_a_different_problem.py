'''
Absolute value of difference between 2 integers.
'''

if __name__ == '__main__':
    import sys

    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, all output below is stderr     |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    for testcase in sys.stdin:
        a, b = [int(i) for i in testcase.split()]
        print('The difference between {} and {} is: '.format(str(a), str(b)),
              end='',
              flush=True,
              file=sys.stderr)
        print(str(abs(a - b)))
