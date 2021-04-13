'''
Reorder input

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    numbers = [int(i) for i in input().split()]
    numbers.sort()

    result = ''
    for glyph in input():
        if result:
            result += ' '
        result += str(numbers[ord(glyph) - ord('A')])

    print(result)

###############################################################################

if __name__ == '__main__':
    main()
