'''
Use Fenwick tree to manage operations and queries.

Status: Time Limit Exceeded
'''

import sys

###############################################################################

def create_tree(nodes):
    '''Create binary indexed tree as a list.'''

    return [0] * (nodes + 1)

###############################################################################

def change_value(binary_indexed_tree, index, amount):
    '''Modify the binary indexed tree.'''

    index += 1
    while index < len(binary_indexed_tree):
        binary_indexed_tree[index] += amount
        index += ((index) & -(index))  # Least Significant Bit

###############################################################################

def query_value(binary_indexed_tree, index):
    '''Query value of the binary indexed tree at a given index.'''

    result = 0
    while index > 0:
        result += binary_indexed_tree[index]
        index -= ((index) & -(index))  # Least Significant Bit
    return result

###############################################################################

FLATTENED = True

if __name__ == '__main__':
    if FLATTENED:
        inputlines = sys.stdin.readlines()
        array_length, queries = [int(i) for i in inputlines[0].split()]
        binary_indexed_tree = [0] * (array_length + 1)

        for query in range(1, 1 + queries):
            text = inputlines[query].split()
            if text[0] == '+':
                index = 1 + int(text[1])
                amount = int(text[2])
                while index < len(binary_indexed_tree):
                    binary_indexed_tree[index] += amount
                    index += ((index) & -(index))  # Least Significant Bit
            elif text[0] == '?':
                result = 0
                index = int(text[1])
                while index > 0:
                    result += binary_indexed_tree[index]
                    index -= ((index) & -(index))  # Least Significant Bit
                print(result)
    else:
        STDERROR_HEADER = \
        '''
        +---------------------------------------------------------------------+
        | If stderr is displayed and out of sync, then all below is stderr.   |
        +---------------------------------------------------------------------+
        '''
        print(STDERROR_HEADER, file=sys.stderr)

        inputlines = sys.stdin.readlines()
        array_length, queries = [int(i) for i in inputlines[0].split()]
        binary_indexed_tree = create_tree(array_length)

        for query in inputlines[1:]:
            text = query.split()
            if text[0] == '+':
                change_value(binary_indexed_tree, int(text[1]), int(text[2]))
            elif text[0] == '?':
                print('{} {} = '.format(text[0], text[1]),
                      end='',
                      flush=True,
                      file=sys.stderr)
                print(query_value(binary_indexed_tree, int(text[1])))

###############################################################################
