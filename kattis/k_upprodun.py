'''
Determine room layout of teams displayed as asterisks

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output of asterisks"""

    rooms = int(input())
    teams = int(input())

    stars = teams // rooms
    larges = teams % rooms

    result_1 = ['*' * (stars + 1)] * larges
    result_2 = ['*' * stars] * (rooms - larges)
    print('\n'.join(result_1 + result_2))

###############################################################################

if __name__ == '__main__':
    main()
