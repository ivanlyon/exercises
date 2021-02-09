'''
Detect lower case characters in any but the first position of many strings

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    problems, tests = [int(i) for i in input().split()]
    solve = 0
    for _ in range(problems):
        faults = 0
        for _2 in range(tests):
            if not input()[1:].islower():
                faults += 1
        if not faults:
            solve += 1

    print(solve)

###############################################################################

if __name__ == '__main__':
    main()
