"""
Maximum value of 0-1 knapsack

Status: Time Limit Exceeded
"""

import copy
import sys
from collections import namedtuple

Item = namedtuple('Item', ['value', 'weight', 'index'])

###############################################################################

def knapsack(items, capacity, is_demo=False):
    """Deliver packed items of maximum value"""

    items.sort(key=lambda per: per.value / per.weight, reverse=True)
    memo = [[] for _ in range(len(items) + 1)]
    packed = copy.copy(memo)
    capacity1 = capacity + 1
    memo[0] = [0] * capacity1
    packed[0] = [False] * capacity1
    for row, in_hand in enumerate(items, start=1):
        memo[row] = copy.copy(memo[row - 1])
        packed[row] = copy.copy(packed[0])
        comparisons = capacity1 - in_hand.weight
        if comparisons > 0:
            for index, diff in enumerate(zip(memo[row - 1][:comparisons], memo[row][capacity1 - comparisons:]), start=in_hand.weight):
                if in_hand.value > diff[1] - diff[0]:
                    memo[row][index] = in_hand.value + diff[0]
                    packed[row][index] = True

    results = []
    trying = len(items)
    in_capacity = capacity
    while trying and in_capacity:
        if packed[trying][in_capacity]:
            results.append(items[trying - 1].index)
            in_capacity -= items[trying - 1].weight
        trying -= 1

    if is_demo:
        history = []
        trying = len(items)
        in_capacity = capacity
        while trying and in_capacity:
            if packed[trying][in_capacity]:
                history.append((trying, in_capacity))
                in_capacity -= items[trying - 1].weight
            trying -= 1

        return results, packed[1:], history

    return results

###############################################################################

def main(inorder=False):
    """Read input for knapsack()"""

    numbers = []
    for i in sys.stdin.read().splitlines():
        numbers += [int(k) for k in i.split()]

    index = 0
    len_numbers = len(numbers)
    while index < len_numbers:
        capacity, objects = numbers[index], numbers[index + 1]
        index += 2

        object_list = []
        for count in range(objects):
            object_list.append(Item(numbers[index], numbers[index + 1], count))
            index += 2

        results = knapsack(object_list, capacity)
        print(str(len(results)))
        if inorder:
            print(' '.join([str(i) for i in sorted(results)]))
        else:
            print(' '.join([str(i) for i in results]))

###############################################################################

def demo():
    '''Knapsack demonstration with random contents'''
    import matplotlib.pyplot as plt
    import random

    max_weight = 25
    object_list = []
    objects = random.randint(18, 20)
    capacity = random.randint(20, max_weight)
    for count in range(objects):
        random_weight = random.randint(1, max_weight)
        random_value = random.randint(1, 100)
        object_list.append(Item(random_value, random_weight, count))

    packing_list, packed, path = knapsack(object_list, capacity, is_demo=True)

    best_value = sum([i.value for i in object_list if i.index in packing_list])
    headline = 'Items "' + ' '.join([str(i) for i in packing_list]) + \
               '" with maximal value ' + str(best_value)
    print(headline)

    val_wt = [str(obj.value) + ',' + str(obj.weight) for obj in object_list]
    row_labels = []
    for index, text in enumerate(val_wt):
        row_labels.append(str(object_list[index].index) + ': ' + text)
    column_labels = [str(i) for i in range(capacity + 1)]
    cell_labels = []
    for row in packed:
        cell_labels.append([str(r)[0] for r in row])

    _fig, axes = plt.subplots()
    plt.suptitle('Knapsack Demonstration (Note sort by value:weight)', fontweight='bold')
    axes.set_title(headline)
    axes.set_axis_off()
    table = axes.table(
        cellText=cell_labels,
        rowLabels=row_labels,
        colLabels=column_labels,
        rowColours=["lightblue"] * (objects),
        colColours=["lightblue"] * (capacity + 1),
        cellLoc='center',
        rowLoc='left',
        loc='center')

    for cell in table.get_children():
        cell_text = cell.get_text().get_text()
        if cell_text == 'T':
            cell.set_facecolor("palegreen")

    for final in path:
        table[final].set_facecolor("red")

    plt.show()

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="0-1 knapsack demonstration", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
