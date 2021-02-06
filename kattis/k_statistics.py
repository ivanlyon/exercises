'''
Produce minimum, maximum and the difference of number list

Status: Accepted
'''

###############################################################################

def read_line_of_integers():
    """Read one line of numbers or detect EOF"""

    try:
        text = input()
        return [int(i) for i in text.split()][1:]
    except EOFError:
        pass

    return None

###############################################################################

def main():
    """Read input and print output statistics about list of numbers"""

    test_case = 0
    while True:
        numbers = read_line_of_integers()
        if numbers:
            test_case += 1
            mini = min(numbers)
            maxi = max(numbers)
            print('Case {0}: {1} {2} {3}'.format(test_case, mini, maxi, maxi - mini))
        else:
            break

###############################################################################

if __name__ == '__main__':
    main()
