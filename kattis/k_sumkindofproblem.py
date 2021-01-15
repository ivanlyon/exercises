'''
Determine sums of integer series derived from input parameter

Status: Accepted
'''
import sys

###############################################################################

def main():
    """Read input and print output for sums of integer series"""

    testcases = sys.stdin.readline()
    for _ in range(int(testcases.strip())):
        testcase, value = [int(i) for i in sys.stdin.readline().split()]
        sum3 = value * (value + 1)
        sum2 = sum3 - value
        sum1 = sum3 >> 1
        print(' '.join([str(i) for i in [testcase, sum1, sum2, sum3]]))

###############################################################################

if __name__ == '__main__':
    main()
