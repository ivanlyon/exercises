'''
Print initials

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    result = ''
    for name in input().split('-'):
        result += name[0]
    print(result)

###############################################################################

if __name__ == '__main__':
    main()
