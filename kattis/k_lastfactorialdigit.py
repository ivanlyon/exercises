'''
Last digit of number's factorial

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    nonzero = {}
    nonzero[1] = 1
    nonzero[2] = 2
    nonzero[3] = 6
    nonzero[4] = 4
    for _ in range(int(input())):
        i = int(input())
        if i in nonzero:
            print(nonzero[i])
        else:
            print('0')

###############################################################################

if __name__ == '__main__':
    main()
