'''
8 queens validation

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    queens = []
    for row in range(8):
        for col, square in enumerate(input()):
            if square == '*':
                queens.append((row, col))

    if len(queens) != 8:
        print("invalid")
        return

    for i in queens:
        for j in queens:
            if i != j:
                dy = abs(i[0] - j[0])
                dx = abs(i[1] - j[1])
                if dy == 0 or dx == 0 or dy == dx:
                    print("invalid")
                    return

    print("valid")

###############################################################################

if __name__ == '__main__':
    main()
