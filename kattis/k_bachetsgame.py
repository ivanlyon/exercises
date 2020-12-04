'''
Determine perfect play winner of Bachet's game given players stan & ollie. This
is a normal nim game where the winner is the last person to make a move.

Status: Accepted
'''

import sys

###############################################################################

def nimNormal(stones, quants):
    '''Normal nim game where stones removed must be a listed value.'''
    UNKNOWN = 0
    FIRST = 1 # ID of 1st player to draw
    SECOND = 2 # ID of 2nd drawing player
    LIMIT = stones - max(quants)
    winner = [UNKNOWN for i in range(stones + 1)]

    for s in range(LIMIT):
        if winner[s] == UNKNOWN:
            winner[s] = SECOND
            for q in quants:
                winner[s + q] = FIRST

    for s in range(LIMIT, stones + 1):
        if winner[s] == UNKNOWN:
            winner[s] = SECOND
            for q in quants:
                if s + q <= stones:
                    winner[s + q] = FIRST
            if winner[stones] != UNKNOWN:
                break

    if winner[stones] == SECOND:
        return "Ollie wins"
    else:
        return "Stan wins"

###############################################################################

if __name__ == '__main__':
    for testCase in sys.stdin:
        inputs = [int(i) for i in testCase.split()]
        print(nimNormal(inputs[0], inputs[2:]))

###############################################################################
