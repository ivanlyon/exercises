'''
Determine best possible result of peg solitaire game

Status: Accepted
'''

import copy
from collections import namedtuple

Coord = namedtuple('Coord', ['row', 'column'])

PEGS, BOARD = None, None

###############################################################################

def read_board():
    """Read one peg board"""

    global BOARD, PEGS
    BOARD, PEGS = [], []
    row, columns = 0, 0
    while True:
        try:
            text = input()
            if text:
                BOARD.append(list(text))
                for column, glyph in enumerate(text):
                    if glyph == 'o':
                        PEGS.append(Coord(row, column))
                columns = max(columns, column)
            else:
                break
        except EOFError:
            break
        row += 1

    # Even out rhs
    for index in range(row):
        BOARD[index] = BOARD[index] + ['#'] * (columns - len(BOARD[index]) + 1)

    while len(BOARD) < 3:
        BOARD.append(['#'] * columns)

    return len(PEGS)

###############################################################################

def add_peg(location):
    """Add a peg to the board and update all global variables accordingly"""

    global PEGS, BOARD
    BOARD[location.row][location.column] = 'o'
    PEGS.append(location)

###############################################################################

def rem_peg(location):
    """Remove peg to the board and update all global variables accordingly"""

    global PEGS, BOARD
    BOARD[location.row][location.column] = '.'
    PEGS.remove(location)

###############################################################################

def dfs():
    """Depth First Search for minimal peg solution"""

    global PEGS, BOARD
    minimal_pegs = len(PEGS)
    if minimal_pegs > 1:
        for moving in copy.copy(PEGS):
            rem_peg(moving)
            if moving.row > 1 and BOARD[moving.row - 2][moving.column] == '.' and BOARD[moving.row - 1][moving.column] == 'o':
                add_peg(Coord(moving.row - 2, moving.column))
                rem_peg(Coord(moving.row - 1, moving.column))
                minimal_pegs = min(minimal_pegs, dfs())
                if minimal_pegs == 1:
                    return 1
                rem_peg(Coord(moving.row - 2, moving.column))
                add_peg(Coord(moving.row - 1, moving.column))
            if moving.column > 1 and BOARD[moving.row][moving.column - 2] == '.' and BOARD[moving.row][moving.column - 1] == 'o':
                add_peg(Coord(moving.row, moving.column - 2))
                rem_peg(Coord(moving.row, moving.column - 1))
                minimal_pegs = min(minimal_pegs, dfs())
                if minimal_pegs == 1:
                    return 1
                rem_peg(Coord(moving.row, moving.column - 2))
                add_peg(Coord(moving.row, moving.column - 1))
            if moving.row + 2 < len(BOARD) and BOARD[moving.row + 2][moving.column] == '.' and BOARD[moving.row + 1][moving.column] == 'o':
                add_peg(Coord(moving.row + 2, moving.column))
                rem_peg(Coord(moving.row + 1, moving.column))
                minimal_pegs = min(minimal_pegs, dfs())
                if minimal_pegs == 1:
                    return 1
                rem_peg(Coord(moving.row + 2, moving.column))
                add_peg(Coord(moving.row + 1, moving.column))
            if moving.column + 2 < len(BOARD[0]) and BOARD[moving.row][moving.column + 2] == '.' and BOARD[moving.row][moving.column + 1] == 'o':
                add_peg(Coord(moving.row, moving.column + 2))
                rem_peg(Coord(moving.row, moving.column + 1))
                minimal_pegs = min(minimal_pegs, dfs())
                if minimal_pegs == 1:
                    return 1
                rem_peg(Coord(moving.row, moving.column + 2))
                add_peg(Coord(moving.row, moving.column + 1))
            add_peg(moving)

    return minimal_pegs

###############################################################################

def main():
    """Read input and print best possible score of peg solitaire game"""

    for _ in range(int(input())):
        input_pegs = read_board()
        minimal_pegs = dfs()
        print(minimal_pegs, input_pegs - minimal_pegs)

###############################################################################

if __name__ == '__main__':
    main()
