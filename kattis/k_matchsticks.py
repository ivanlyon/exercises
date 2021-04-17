'''
Minimum and maximum numbers made of matchsticks

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    precomputed = {}
    precomputed[2] = 1
    precomputed[3] = 7
    precomputed[4] = 4
    precomputed[5] = 2
    precomputed[6] = 6
    precomputed[7] = 8
    precomputed[8] = 10
    precomputed[9] = 18
    precomputed[10] = 22
    precomputed[11] = 20
    precomputed[12] = 28
    precomputed[13] = 68
    precomputed[14] = 88
    precomputed[15] = 108
    precomputed[16] = 188
    precomputed[17] = 200
    for _ in range(int(input())):
        sticks = int(input())

        if sticks in precomputed:
            low_string = str(precomputed[sticks])
        else:
            eights = (sticks - 11) // 7
            low_string = str(precomputed[sticks - eights * 7]) + '8' * eights

        ones = (sticks // 2) - 1
        high_string = str(precomputed[sticks - 2 * ones]) + '1' * ones

        print(low_string, high_string)

###############################################################################

if __name__ == '__main__':
    main()
