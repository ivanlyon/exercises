'''
Determine perfect play winner of Bachet's game given players stan & ollie.

Status: Time Limit Exceeded (> 1.0s)
'''

import sys

###############################################################################

def playGame(stones, quants):
    '''Determine winner of bachet's game (Stan draws 1st)'''
    ollies = set([0])
    quants = sorted(quants)
    for s in range(1, stones + 1):
        lastDraw = False
        for q in quants:
            if (s - q) in ollies:
                lastDraw = True
                break
        if not lastDraw:
            ollies.add(s)

    if stones in ollies:
        return "Ollie wins"
    else:
        return "Stan wins"

###############################################################################

def playGameTLE(stones, quants):
    '''Determine winner of bachet's game (Stan draws 1st)'''
    ollies = set([0])
    for s in range(1, stones + 1):
        lastDraw = False
        for q in quants:
            if (s - q) in ollies:
                lastDraw = True
                break
        if not lastDraw:
            ollies.add(s)

    if stones in ollies:
        return "Ollie wins"
    else:
        return "Stan wins"

###############################################################################

if __name__ == '__main__':
    for testCase in sys.stdin:
        inputs = [int(i) for i in testCase.split()]
        print(playGame(inputs[0], inputs[2:]))

###############################################################################
