'''
Determine whether a factorial is evenly divisible by a number.

Status: Accepted
'''

from math import gcd
from collections import Counter

###############################################################################

def pollard_rho(number):
    """Produce random factor of number"""

    bits = ((number - 1) & (1 - number)).bit_length() - 1
    exponent = number >> bits
    for attempt in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if attempt % number:
            product = pow(attempt, exponent, number)
            if product in (1, number - 1):
                continue
            for _ in range(bits):
                prev = product
                product = (product * product) % number
                if product == number - 1:
                    break
                if product == 1:
                    return gcd(prev - 1, number)
            else:
                for iteration in range(2, number):
                    x, y = iteration, (iteration * iteration + 1) % number
                    factor = gcd(abs(x - y), number)
                    while factor == 1:
                        x, y = (x * x + 1) % number, (y * y + 1) % number
                        y = (y * y + 1) % number
                        factor = gcd(abs(x - y), number)
                    if factor != number:
                        return factor

    return number

###############################################################################

def prime_factors(number):
    """Return Counter of the prime factorization of number"""

    if number <= 1:
        return Counter()

    term = pollard_rho(number)
    if number == term:
        return Counter([number])

    return prime_factors(term) + prime_factors(number // term)

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            facts, denominator = [int(i) for i in input().split()]
        except EOFError:
            break

        if denominator:
            divisible = (denominator == 1 or facts >= denominator)
            if not divisible:
                divisor = denominator
                easy_factors = Counter()
                while divisor & 1 == 0:
                    easy_factors += Counter([2])
                    divisor >>= 1
                while divisor % 3 == 0:
                    easy_factors += Counter([3])
                    divisor //= 3
                divprimes = easy_factors + prime_factors(divisor)

                divisible = True
                for div in divprimes:
                    count, term = 0, 1
                    for _ in range(divprimes[div]):
                        term *= div
                        count += facts // term
                    if count < divprimes[div]:
                        divisible = False
                        break
        else:
            divisible = False

        if divisible:
            print('{0} divides {1}!'.format(denominator, facts))
        else:
            print('{0} does not divide {1}!'.format(denominator, facts))

###############################################################################

if __name__ == '__main__':
    main()
