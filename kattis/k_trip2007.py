'''
Determine optimal packing of objects (Greedy)

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    bag = None
    while True:
        bags = int(input())
        if bags == 0:
            break

        if not bag is None:
            print()
        bag = Counter()
        while bags != sum(bag.values()):
            bag += Counter([int(i) for i in input().split()])

        max_frequency = bag.most_common()[0][1]
        nesting = (bags + max_frequency - 1) // max_frequency # int ceil
        uneven = bags % max_frequency

        print(max_frequency)
        while bags:
            result = [i[0] for i in bag.most_common(nesting)]
            for piece in result:
                bag[piece] -= 1
            print(' '.join([str(i) for i in result]))
            bags -= len(result)

            if uneven:
                uneven -= 1
                if not uneven:
                    nesting -= 1

###############################################################################

if __name__ == '__main__':
    main()
