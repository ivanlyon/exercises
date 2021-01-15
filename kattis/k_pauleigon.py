'''
Determine server given times served by 2 players.

Status: Accepted
'''

###############################################################################

def main():
    """Predict server given times served"""

    n, p, q = map(int, input().strip().split())
    if (p + q) % (n + n) < n:
        print("paul")
    else:
        print("opponent")

###############################################################################

if __name__ == '__main__':
    main()
