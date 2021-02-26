'''
A process not a problem

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        input() # blank line
        input() # unnecessary numbers
        godzillas = [int(i) for i in input().split()]
        mechas = [int(i) for i in input().split()]
        if max(godzillas) >= max(mechas):
            print('Godzilla')
        else:
            print('MechaGodzilla')

###############################################################################

if __name__ == '__main__':
    main()
