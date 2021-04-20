'''
Count number of paired equal division results

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    square_minus_1 = lambda a: (a * (a - 1))
    _numerators, denominator = [int(_) for _ in input().split()]
    results = Counter()
    for i in map(int, input().split()):
        results[i // denominator] += 1

    sum_of_products = 0
    for i in results:
        sum_of_products += square_minus_1(results[i])
    print(sum_of_products >> 1)

###############################################################################

if __name__ == '__main__':
    main()
