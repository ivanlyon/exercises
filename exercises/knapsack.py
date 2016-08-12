'''
0-1 Knapsack dynamic programming algorithm.

Input:
------
    The first line contains a single integer for W, the weight limit of the
knapsack.  The second line contains the N, the number of items to be
considered for packing into the knapsack.
  +------------------------------------------------------------------+
  | 112                                                              |
  | 8                                                                |
  | 21 10                                                            |
  | 43 22                                                            |
  | 55 26                                                            |
  | 80 40                                                            |
  | 38 20                                                            |
  | 18 8                                                             |
  | 100 51                                                           |
  | 62 33                                                            |
  +------------------------------------------------------------------+

Output:
-------
    For each test case, the result will displayed on a line.
  +------------------------------------------------------------------+
  | Best possible value: 220 achieved with 111 weight                |
  | Knapsack Optimal Packing List:                                   |
  | Appearance Number: 0, Value: 21, Weight: 10                      |
  | Appearance Number: 1, Value: 43, Weight: 22                      |
  | Appearance Number: 4, Value: 38, Weight: 20                      |
  | Appearance Number: 5, Value: 18, Weight: 8                       |
  | Appearance Number: 6, Value: 100, Weight: 51                     |
  +------------------------------------------------------------------+
'''

###############################################################################

def knapsack(items, maxweight):
    """
    Computes the most valuable subsequence of items weighing no more than
    maxweight.

    items is a sequence of value pairs.  Each pair consists of the item value
    followed by the item weight.
    """

    # maxvalue[i][w] is the best sum of values for any subsequence of the
    # first i items, whose weights sum to no more than w.
    maxvalue = [[0] * (maxweight + 1) for _ in range(len(items) + 1)]

    for i, (value, weight) in enumerate(items, 1):
        for packed_weight in range(maxweight + 1):
            if weight > packed_weight:
                maxvalue[i][packed_weight] = maxvalue[i - 1][packed_weight]
            else:
                omit = maxvalue[i - 1][packed_weight]
                pack = maxvalue[i - 1][packed_weight - weight] + value
                maxvalue[i][packed_weight] = max(pack, omit)

    choices = []
    w = maxweight
    for i in range(len(items), 0, -1):
        if maxvalue[i][w] != maxvalue[i - 1][w]:
            choices.append(i - 1)
            w -= items[i - 1][1]

    return sorted(choices)

###############################################################################

if __name__ == '__main__':
    maxweight = int(input())
    items = []
    for i in range(int(input())):
        items.append([int(j) for j in input().split()])

    choices = knapsack(items, maxweight)
    data = []
    for r in choices:
        data.append([r] + items[r])
    _, achieved_value, achieved_weight = list(map(sum, zip(*data)))

    print('Best possible value: {} achieved with {} weight'.format(
        achieved_value, achieved_weight))
    print('Knapsack Optimal Packing List:')
    for i, value, weight in data:
        print('Appearance Number: {}, Value: {}, Weight: {}'.format(i, value, weight))

###############################################################################
