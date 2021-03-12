'''
Determine number of ferry crossings

Status: Accepted
'''

from collections import deque

###############################################################################

def main():
    """Read input and print output"""

    for _test_case in range(int(input())):
        meters, cars = [int(i) for i in input().split()]
        lhs, rhs, crosses = deque([]), deque([]), 0
        for _ in range(cars):
            length, side = input().split()
            if side == 'left':
                lhs.append(int(length))
            else:
                rhs.append(int(length))
        centimeters = 100 * meters
        while lhs or rhs:
            available = centimeters
            if crosses & 0x01:
                while rhs and available >= rhs[0]:
                    available -= rhs.popleft()
                crosses += 1
            else:
                while lhs and available >= lhs[0]:
                    available -= lhs.popleft()
                crosses += 1
        print(crosses)

###############################################################################

if __name__ == '__main__':
    main()
