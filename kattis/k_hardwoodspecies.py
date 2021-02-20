'''
Print percentage of appearances per string in input

Status: Accepted

(Note: not unittest-able with AC input implementation due to TLE)
'''

from sys import stdin
from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    total = 0
    trees = Counter()

    # AC input scheme is faster than input()
#    for line in stdin:
#        trees[line[:-1]] += 1 # strip() may give WA
#        total += 1

    while True:
        try:
            trees[input()] += 1
            total += 1
        except EOFError:
            break

    results = []
    for tree in trees:
        results.append('{0} {1:.6f}'.format(tree, 100 * trees[tree] / total))

    print('\n'.join(sorted(results)))

###############################################################################

if __name__ == '__main__':
    main()
