'''
Estimate Euler's number

Status: Accepted
'''

import math

###############################################################################

def main():
    """Read input and print output"""

    result = 0
    for i in range(min(20, int(input()) + 1)):
        result += 1 / math.factorial(i)

    print('{0:.16}'.format(result))

###############################################################################

if __name__ == '__main__':
    main()
