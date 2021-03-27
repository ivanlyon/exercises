'''
Stan vs Ollie game of multiplication with standard victory.

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    player = 0
    number = [1]
    winner = ['None']
    while number[-1] < 4300000000:
        if player:
            number.append(number[-1] * 2)
            winner.append('Ollie')
        else:
            number.append(number[-1] * 9)
            winner.append('Stan')
        player = 1 - player

    while True:
        try:
            target = int(input())
            for index, value in enumerate(number[1:], start=1):
                if target in range(number[index - 1], value + 1):
                    print(winner[index] + ' wins.')
                    break
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
