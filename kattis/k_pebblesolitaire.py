'''
Optimal result for pebble solitaire state

Status: Accepted
'''

PRECOMPUTED = {}
for _i in range(12):
    PRECOMPUTED['-' * _i + 'o' + '-' * (11 - _i)] = 1

###############################################################################

def dfs(state):
    """Depth First Search for best possible score"""

    global PRECOMPUTED
    if state in PRECOMPUTED:
        return PRECOMPUTED[state]

    score = sum([1 for i in state if i == 'o'])
    for i in range(10):
        if state[i:i + 3] == 'oo-':
            score = min(score, dfs(state[:i] + '--o' + state[i + 3:]))
        if state[i:i + 3] == '-oo':
            score = min(score, dfs(state[:i] + 'o--' + state[i + 3:]))
    PRECOMPUTED[state] = score

    return score

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        print(dfs(input()))

###############################################################################

if __name__ == '__main__':
    main()
