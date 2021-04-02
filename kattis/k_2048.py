'''
2048 game state after single manuever

Status: Accepted
'''

###############################################################################

def zero_shift(four):
    """Shift digits through the zero values as though they are empty"""

    shifting = True
    while shifting:
        shifting = False
        for i in range(3):
            if four[i] == 0 and four[i + 1] != 0:
                four[i] = four[i + 1]
                four[i + 1] = 0
                shifting = True
    return four

###############################################################################

def shift4(four):
    """Shift the digits of a 1 dimension 4 element sequence"""

    four = zero_shift(four)
    for i in range(3):
        if four[i] == four[i + 1]:
            four[i] += four[i + 1]
            four[i + 1] = 0

    return zero_shift(four)

###############################################################################

def rotate_ccw(puzzle):
    """Rotate the puzzle 90 degrees counter-clockwise"""

    result = []
    for col in reversed(range(4)):
        temp = []
        for row in range(4):
            temp.append(puzzle[row][col])
        result.append(temp)
    return result

###############################################################################

def main():
    """Read input and print output"""

    puzzle = []
    for _ in range(4):
        puzzle.append([int(i) for i in input().split()])

    direction = int(input())
    for _ in range(direction):
        puzzle = rotate_ccw(puzzle)

    for row in range(4):
        puzzle[row] = shift4(puzzle[row])

    while direction not in [0, 4]:
        puzzle = rotate_ccw(puzzle)
        direction += 1

    for row in puzzle:
        print(' '.join([str(i) for i in row]))

###############################################################################

if __name__ == '__main__':
    main()
