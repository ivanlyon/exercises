'''
Decimal printed to parameter precision

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    glyph = {}
    for i in range(10):
        glyph[i] = str(i)

    while True:
        try:
            numerator, denominator, digits = [int(i) for i in input().split()]
        except EOFError:
            break

        result = ['0', '.'] + digits * ['*']
        for place in range(digits):
            numerator *= 10
            result[place + 2] = glyph[numerator // denominator]
            numerator %= denominator
        print(''.join(result))

###############################################################################

if __name__ == '__main__':
    main()
