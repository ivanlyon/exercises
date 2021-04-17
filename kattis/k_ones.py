'''
Smallest factor to reach a number composed of digit '1'

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            number = int(input())
        except EOFError:
            break

        if number == 1:
            print('1')
        else:
            assert number % 2 != 0
            assert number % 5 != 0
            digits, remainder = 1, 1
            while remainder:
                remainder = (remainder * 10 + 1) % number
                digits += 1
            print(digits)

###############################################################################

if __name__ == '__main__':
    main()
