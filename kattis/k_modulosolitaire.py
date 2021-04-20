'''
Minimal transitions to zero

Status: Accepted
'''

from collections import deque

###############################################################################

def main():
    """Read input and print output"""

    modulus, branches, start_value = [int(_) for _ in input().split()]
    a_value, b_value = [None] * branches, [None] * branches
    for i in range(branches):
        a_value[i], b_value[i] = [int(_) for _ in input().split()]

    moves = [0] * modulus
    moves[start_value] = 1
    bfsq = deque([start_value])
    while bfsq:
        start_value = bfsq.popleft()
        for i in range(branches):
            next_value = (start_value * a_value[i] + b_value[i]) % modulus
            if not moves[next_value]:
                moves[next_value] = moves[start_value] + 1
                bfsq.append(next_value)
        if moves[0]:
            break

    print(moves[0] - 1)

###############################################################################

if __name__ == '__main__':
    main()
