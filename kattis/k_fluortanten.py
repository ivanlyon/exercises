'''
Maximum sum with modified positions

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    _ = input()
    numbers = list(map(int, input().split()))

    unmoved, zero_index = 0, numbers.index(0)
    for coeff, i in enumerate(numbers, start=1):
        unmoved += coeff * i

    maximal, nsum = unmoved, unmoved
    for i in numbers[zero_index + 1:]:
        nsum -= i
        maximal = max(nsum, maximal)

    nsum = unmoved
    for i in reversed(numbers[:zero_index]):
        nsum += i
        maximal = max(nsum, maximal)

    print(maximal)

###############################################################################

if __name__ == '__main__':
    main()
