'''
Detect divergent position with given number of iterations

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    modulus = lambda c: (c.real*c.real + c.imag*c.imag)
    test_case = 0
    while True:
        try:
            _r, _i, iterations = input().split()
        except EOFError:
            break

        position = complex(float(_r), float(_i))
        z_value, outside = complex(0.0, 0.0), False
        for _ in range(int(iterations)):
            z_next = z_value * z_value + position
            outside = (modulus(z_next) > 4)
            if outside:
                break
            z_value = z_next

        test_case += 1
        print('Case {0}: {1}'.format(test_case, 'OUT' if outside else 'IN'))

###############################################################################

if __name__ == '__main__':
    main()
