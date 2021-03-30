'''
Rock Paper Scissors tournament results

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    blank_line = False
    while True:
        parameter = input()
        if parameter == '0':
            break

        if blank_line:
            print()
        blank_line = True

        players, games = map(int, parameter.split())
        wins = [0] * (players + 1)
        losses = [0] * (players + 1)
        player = [0, 0, 0]
        for _ in range((games * players * (players - 1)) >> 1):
            player[1], rps1, player[2], rps2 = input().split()
            if rps1 != rps2:
                winner = 0 # Avoids lint message
                if rps1 == 'rock':
                    winner = 1 if rps2 == 'scissors' else 2
                if rps1 == 'paper':
                    winner = 1 if rps2 == 'rock' else 2
                if rps1 == 'scissors':
                    winner = 1 if rps2 == 'paper' else 2
                wins[int(player[winner])] += 1
                losses[int(player[3 - winner])] += 1

        results = []
        for pair in zip(wins, losses):
            if pair[0] + pair[1]:
                results.append('{0:.3f}'.format(pair[0] / (pair[0] + pair[1])))
            else:
                results.append('-')

        print('\n'.join(results[1:]))

###############################################################################

if __name__ == '__main__':
    main()
