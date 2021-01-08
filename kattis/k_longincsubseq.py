'''
Determine indexes of the Longest Increasing Subsequence

Status: Accepted
'''
import sys
from bisect import bisect

###############################################################################

def longest_inc_subseq(sequence):
    '''Determine indexes of the Longest Increasing Subsequence'''

    len_sequence = len(sequence)
    exceeded = [0] * len_sequence
    lis_place = [0] * (len_sequence + 1)

    lis = [sequence[0]]
    len_lis = 1
    longest_place = 0
    for place, value in enumerate(sequence[1:], start=1):
        if value < lis[0]:
            index = 0
        elif lis[-1] < value:
            index = len_lis
        else:
            index = bisect(lis, value) # index is rhs of existing 'value'
            if lis[index - 1] == value:
                index = -1

        if index >= 0:
            if index == len_lis:
                lis.append(value)
                len_lis += 1
                longest_place = place
            else:
                lis[index] = value

            exceeded[place] = lis_place[index - 1]
            lis_place[index] = place

    result = [0] * len_lis
    place = longest_place
    for index in range(len_lis - 1, -1, -1):
        result[index] = place
        place = exceeded[place]

    return result

###############################################################################

def main():
    """Read input and print output of longest_inc_subseq()"""

    # Create buffer of all input numbers
    numbers = []
    for i in sys.stdin.read().splitlines():
        numbers += [int(k) for k in i.split()]
    at_number = 0
    len_numbers = len(numbers)

    while at_number < len_numbers:
        inputs = numbers[at_number]
        at_number += 1

        items = []
        for _ in range(inputs):
            items.append(numbers[at_number])
            at_number += 1

        results = longest_inc_subseq(items)
        print(str(len(results)))
        print(' '.join([str(_) for _ in results]))

###############################################################################

if __name__ == '__main__':
    main()
