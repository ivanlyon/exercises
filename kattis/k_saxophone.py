'''
Count saxophone button presses

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    pressing = {}
    pressing['c'] = [2, 3, 4, 7, 8, 9, 10]
    pressing['d'] = [2, 3, 4, 7, 8, 9]
    pressing['e'] = [2, 3, 4, 7, 8]
    pressing['f'] = [2, 3, 4, 7]
    pressing['g'] = [2, 3, 4]
    pressing['a'] = [2, 3]
    pressing['b'] = [2]
    pressing['C'] = [3]
    pressing['D'] = [1, 2, 3, 4, 7, 8, 9]
    pressing['E'] = [1, 2, 3, 4, 7, 8]
    pressing['F'] = [1, 2, 3, 4, 7]
    pressing['G'] = [1, 2, 3, 4]
    pressing['A'] = [1, 2, 3]
    pressing['B'] = [1, 2]
    for _ in range(int(input())):
        totals, pressed = [0] * 11, [False] * 11
        for note in input():
            for button, is_down in enumerate(pressed):
                if is_down and button not in pressing[note]:
                    pressed[button] = False
            for button in pressing[note]:
                if not pressed[button]:
                    totals[button] += 1
                    pressed[button] = True
        print(' '.join([str(i) for i in totals[1:]]))

###############################################################################

if __name__ == '__main__':
    main()
