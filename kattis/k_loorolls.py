'''
Determine both scores of a programming contest team

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    roll, usage = [int(i) for i in input().split()]
    rolls, remaining = 1, roll % usage
    while remaining:
        usage -= remaining
        rolls += 1
        remaining = roll % usage
    print(rolls)

###############################################################################

if __name__ == '__main__':
    main()
