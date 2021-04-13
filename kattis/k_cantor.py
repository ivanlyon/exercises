'''
Detect Cantor set membership

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        value = input()
        if value == 'END':
            break
        value = float(value)

        lhs, rhs, ternary = 0.0, 1.0, ''
        for _ in range(12):
            third = (rhs - lhs) / 3
            if value <= lhs + third:
                ternary += '0'
                rhs = lhs + third
            elif value >= rhs - third:
                ternary += '2'
                lhs = rhs - third
            else:
                ternary += '1'
                break

        if ternary[-1] == '1':
            print('NON-MEMBER')
        else:
            print('MEMBER')

###############################################################################

if __name__ == '__main__':
    main()
