'''
8 * 9 ** (number - 1) all mod 1000000007

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    modulus = 1000000007
    for _ in range(int(input())):
        print((8 * pow(9, int(input()) - 1, modulus)) % modulus)

###############################################################################

if __name__ == '__main__':
    main()
