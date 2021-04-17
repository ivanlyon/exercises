'''
Order a range of integers

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    length = int(input())
    next_print, result = 1, []
    for index, move in enumerate(input(), start=1):
        if move == 'R':
            result += reversed(range(next_print, index + 1))
            next_print = index + 1
    result += reversed(range(next_print, length + 1))
    print('\n'.join(map(str, result)))

###############################################################################

if __name__ == '__main__':
    main()
