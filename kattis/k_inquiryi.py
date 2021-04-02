'''
Maximal value of product between sum of sequential squares and remaining sum.

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    length = int(input())
    a_num, sum1, sum2 = [0] * length, 0, 0
    for k in range(length):
        a_num[k] = int(input())
        sum2 += a_num[k] * a_num[k]

    result = 0
    for k in reversed(range(length)):
        sum2 -= a_num[k] * a_num[k]
        sum1 += a_num[k]
        result = max(result, sum2 * sum1)

    print(result)

###############################################################################

if __name__ == '__main__':
    main()
