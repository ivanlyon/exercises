'''
Smallest number when decomposed into digits for multiplication produces input

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    glyphs = '0123456789'
    while True:
        number = int(input())
        if number == -1:
            break

        if number < 10:
            print(10 + number)
        else:
            divisors = Counter()
            for digit in range(9, 1, -1):
                while number % digit == 0:
                    divisors[digit] += 1
                    number //= digit

            if number == 1:
                result = ''
                for digit in range(2, 10):
                    result += glyphs[digit] * divisors[digit]
                print(result)
            else:
                print('There is no such number.')

###############################################################################

if __name__ == '__main__':
    main()
