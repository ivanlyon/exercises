'''
Determine number's most common factor, in case of tie choose smallest value.

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

    number = int(input())

    easy_factors = Counter()
    while number & 1 == 0:
        easy_factors += Counter([2])
        number >>= 1
    while number % 3 == 0:
        easy_factors += Counter([3])
        number //= 3
    factors = easy_factors + prime_factors(number)

    maximal = factors.most_common(1)[0]
    for number in factors:
        if maximal[1] == factors[number] and maximal[0] > number:
            maximal = number

    print(maximal[0])

###############################################################################

if __name__ == '__main__':
    main()
