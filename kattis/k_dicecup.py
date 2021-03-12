'''
Determine most likely dice sums

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    die1, die2 = [int(i) for i in input().split()]
    sums = Counter()
    for i in range(1, die1 + 1):
        for j in range(1, die2 + 1):
            sums[i + j] += 1
    max_freq = sums.most_common(1)[0]
    for result in sums.most_common():
        if result[1] == max_freq[1]:
            print(result[0])

###############################################################################

if __name__ == '__main__':
    main()
