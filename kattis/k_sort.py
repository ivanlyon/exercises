'''
Sort list of integers by number of appearances and order of appearance

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    result = []
    input() # Unnecessary contents
    numbers = Counter([int(i) for i in input().split()])
    while numbers:
        number, times = numbers.most_common(1)[0]
        result += [number] * times
        del numbers[number]
    print(' '.join([str(i) for i in result]))

###############################################################################

if __name__ == '__main__':
    main()
