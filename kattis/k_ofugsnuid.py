'''
Print input integers in reverse order

Status: Accepted
'''
import sys

###############################################################################

def main():
    """Reverse the order of fixed number of input integers"""

    numbers = []
    for i in sys.stdin.read().splitlines():
        numbers += [int(k) for k in i.split()]
    reversing = numbers[1:1 + numbers[0]]

    print('\n'.join([str(_) for _ in reversing[::-1]]))

###############################################################################

if __name__ == '__main__':
    main()
