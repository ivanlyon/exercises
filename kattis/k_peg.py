'''
Determine number of next moves possible in game of peg

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output number of next moves in game of peg"""

    board = []
    for _ in range(7):
        board.append(input())

    result = 0
    for row in range(7):
        for col in range(7):
            if board[row][col] == 'o':
                if row > 1 and board[row - 1][col] == 'o' and board[row - 2][col] == '.':
                    result += 1
                if col > 1 and board[row][col - 1] == 'o' and board[row][col - 2] == '.':
                    result += 1
                if row < 5 and board[row + 1][col] == 'o' and board[row + 2][col] == '.':
                    result += 1
                if col < 5 and board[row][col + 1] == 'o' and board[row][col + 2] == '.':
                    result += 1

    print(result)

###############################################################################

if __name__ == '__main__':
    main()
