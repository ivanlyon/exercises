'''
Compute the smallest multiple of set of numbers

Status: Accepted
'''

from math import gcd

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            product = 1
            for term in [int(i) for i in input().split()]:
                common = gcd(product, term)
                product *= term // common
            print(product)
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
