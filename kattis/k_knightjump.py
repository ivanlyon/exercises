'''
Shortest knight path to (0, 0) by BFS

Status: Accepted
'''

from collections import deque, namedtuple

Square = namedtuple('Square', ['r', 'c'])

###############################################################################

def main():
    """Read input and print output"""

    vector = lambda m, r, c: m * 1000000 + r * 1000 + c
    unvector = lambda v: (v // 1000000, (v // 1000) % 1000, v % 1000)

    offset = [-2, -1, 1, 2]
    knight_moves = [Square(r, c) for r in offset for c in offset if abs(r) != abs(c)]
    length, board, bfsq, moves = int(input()), [], None, -1
    for row in range(length):
        board.append(list(input()))
        if 'K' in board[-1]:
            bfsq = deque([vector(0, row, board[-1].index('K'))])
    assert bfsq is not None

    if board[0][0] == 'K':
        bfsq = None
        moves = 0

    while bfsq:
        moves, row, column = unvector(bfsq.popleft())
        for kmi in knight_moves:
            nrow, ncol = row + kmi.r, column + kmi.c
            if nrow in range(length) and ncol in range(length):
                if board[nrow][ncol] == '.':
                    bfsq.append(vector(moves + 1, nrow, ncol))
                    board[nrow][ncol] = '#'
        if board[0][0] == '#':
            moves += 1
            break

    if board[0][0] == '.':
        moves = -1

    print(moves)

###############################################################################

if __name__ == '__main__':
    main()
