'''
Remove alternating quarter-lengths from input string

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        rotated = False
        rotations, text = input().split()
        rotations = int(rotations)
        while rotations:
            quarter = (len(text) >> 2)
            if quarter == 0:
                break

            if rotated:
                text = text[:-quarter]
            else:
                text = text[quarter:]

            rotated = not rotated
            rotations -= 1
        print(text)

###############################################################################

if __name__ == '__main__':
    main()
