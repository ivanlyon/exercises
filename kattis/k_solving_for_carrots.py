'''
Reprinting one field from the input.
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

    a, b = [i.strip() for i in input().split()]
    print('The second number was: ',
          end='',
          flush=True,
          file=sys.stderr)
    print(b)
