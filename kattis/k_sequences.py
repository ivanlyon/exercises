'''
Swap counting

Status: Accepted
'''

###############################################################################

def inversions(constants, variables):
    """Number of swaps"""

    if variables:
        pow2 = pow(2, variables - 1, 1_000_000_007)
        return pow2 * (constants * 2 + variables)
    return constants

###############################################################################

def main():
    """Read input and print output"""

    zeroes, qmarks, swaps = 0, 0, 0
    for glyph in reversed(input()):
        if glyph == '0':
            zeroes += 1
        else:
            if glyph == '1':
                swaps += inversions(zeroes, qmarks)

            if glyph == '?':
                swaps += inversions(zeroes, qmarks) + swaps
                qmarks += 1

            swaps %= 1_000_000_007

    print(swaps)

###############################################################################

if __name__ == '__main__':
    main()
