'''
Maximum slope

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    pairs = int(input())
    pair = [[0.0, 0.0]] * pairs
    for i in range(pairs):
        pair[i] = [float(j) for j in input().split()]
    pair.sort()

    lipschitz = abs((pair[1][1] - pair[0][1]) / (pair[1][0] - pair[0][0]))
    for i in range(2, pairs):
        lipschitz = max(lipschitz, abs((pair[i][1] - pair[i-1][1]) / (pair[i][0] - pair[i-1][0])))
    print('{0:.9f}'.format(lipschitz))

###############################################################################

if __name__ == '__main__':
    main()
