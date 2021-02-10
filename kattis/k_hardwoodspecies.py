'''
Print percentage of appearances per string in input

Status: Time Limit Exceeded
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    trees = Counter()
    while True:
        try:
            trees[input()] += 1
        except:
            break

    total = sum([trees[i] for i in trees])
    results = []
    for tree in trees:
        results.append('{0} {1:.6f}'.format(tree, 100 * trees[tree] / total))

    print('\n'.join(sorted(results)))

###############################################################################

if __name__ == '__main__':
    main()
