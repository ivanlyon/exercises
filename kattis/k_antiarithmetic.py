'''
Detect arithmetic sequence of length 3

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        text = input().split()
        if text[0] == '0':
            break

        numbers = [int(_) for _ in text[1:]]
        length, sequenced = len(numbers), False
        indexed = [(j, i) for i, j in enumerate(numbers)]
        indexes = [i[1] for i in sorted(indexed)]
        for middle in range(length):
            if sequenced:
                break
            lhs, rhs = middle - 1, middle + 1
            imiddle = indexes[middle]
            while lhs >= 0 and rhs < length:
                if (indexes[lhs] > imiddle) != (indexes[rhs] > imiddle):
                    sequenced = True
                    break
                lhs -= 1
                rhs += 1

        print('{}'.format('no' if sequenced else 'yes'))

###############################################################################

if __name__ == '__main__':
    main()
