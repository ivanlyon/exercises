'''
Phone button press computations

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for test_case in range(1, int(input()) + 1):
        _1, buttons, _2 = [int(i) for i in input().split()]
        numbers = sorted([int(i) for i in input().split()], reverse=True)
        result, press, button = 0, 1, buttons
        for number in numbers:
            result += press * number
            button -= 1
            if button == 0:
                button = buttons
                press += 1
        print('Case #{0}: {1}'.format(test_case, result))

###############################################################################

if __name__ == '__main__':
    main()
