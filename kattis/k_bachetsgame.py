'''
Determine perfect play winner of Bachet's game given players stan & ollie. This
is a normal nim game where the winner is the last person to make a move.

Status: Accepted
'''

import sys

###############################################################################

def nim_normal(total_stones, quants):
    '''Normal nim game where stones removed must be a listed value.'''
    unknown = 0
    first = 1 # ID of 1st player to draw
    second = 2 # ID of 2nd drawing player
    limit = total_stones - max(quants)
    winner = [unknown for _ in range(total_stones + 1)]

    for stones in range(limit):
        if winner[stones] == unknown:
            winner[stones] = second
            for amount in quants:
                winner[stones + amount] = first

    for stones in range(limit, total_stones + 1):
        if winner[stones] == unknown:
            winner[stones] = second
            for amount in quants:
                if stones + amount <= total_stones:
                    winner[stones + amount] = first
            if winner[total_stones] != unknown:
                break

    if winner[total_stones] == second:
        return "Ollie wins"
    return "Stan wins"

###############################################################################

if __name__ == '__main__':
    for testCase in sys.stdin:
        inputs = [int(i) for i in testCase.split()]
        print(nim_normal(inputs[0], inputs[2:]))

###############################################################################
