'''
Determine maximum sum of values with time constraint

Status: Accepted
'''

from collections import namedtuple

Pair = namedtuple('Pair', ['cash', 'time'])

###############################################################################

def main():
    """Read input and print output"""

    people, seconds = [int(i) for i in input().split()]
    candidate, best_cash = [], [0] * (seconds + 1)
    for _ in range(people):
        cash, departure = [int(i) for i in input().split()]
        candidate.append(Pair(cash, departure))
    candidate.sort(reverse=True)

    for person in candidate:
        index = person.time
        while index >= 0 and best_cash[index]:
            index -= 1

        if index >= 0:
            best_cash[index] = person.cash

    print(sum(best_cash))

###############################################################################

if __name__ == '__main__':
    main()
