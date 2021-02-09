'''
Stable sort strings by first two characters

Status: Accepted
'''

from functools import cmp_to_key

###############################################################################

def compare(item1, item2):
    """Custom sort function comparing first two string characters"""

    item1, item2 = item1[:2], item2[:2]
    if item1 != item2:
        if item1 > item2:
            return 1
        return -1
    return 0

###############################################################################

def main():
    """Read input and print output"""

    data = None
    while True:
        names = int(input())
        if names == 0:
            break

        if not data is None:
            print()

        data = [None] * names
        for i in range(names):
            data[i] = input()

        for i in sorted(data, key=cmp_to_key(compare)):
            print(i)

###############################################################################

if __name__ == '__main__':
    main()
