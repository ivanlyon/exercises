'''
Determine the number c such that c = ax + by

Status: Accepted
'''

###############################################################################

def egcd(a, b):
    """Computes x, y such that gcd(a,b) = ax + by"""

    if not b:
        return 1, 0

    x, y = egcd(b, a % b)
    return y, x - (a // b * y)

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        a, n, b, m = [int(i) for i in input().split()]
        x, y = egcd(n, m)
        k = n * m
        print((b * x * n + a * y * m) % k, k)

###############################################################################

if __name__ == '__main__':
    main()
