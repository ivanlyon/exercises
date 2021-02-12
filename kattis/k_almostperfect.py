'''
Determine if a number is +/-2 within the sum of its factors

Status: Accepted
'''

from math import gcd
from collections import Counter

###############################################################################

def memodict(function):
    """memoization decorator for a function taking a single argument"""

    class MemoDict(dict):
        """Dict modified to store result on miss"""

        def __missing__(self, key):
            ret = self[key] = function(key)
            return ret

    return MemoDict().__getitem__

###############################################################################

def pollard_rho(number):
    """returns random factor of number"""

    if number & 1 == 0:
        return 2
    if number % 3 == 0:
        return 3

    bits = ((number - 1) & (1 - number)).bit_length() - 1
    exponent = number >> bits
    for attempt in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
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

@memodict
def prime_factors(number):
    """returns a Counter of the prime factorization of number"""

    if number <= 1:
        return Counter()

    factor = pollard_rho(number)
    if factor == number:
        return Counter([number])

    return prime_factors(factor) + prime_factors(number // factor)

###############################################################################

def distinct_factors(number):
    """returns a list of all distinct factors of number"""

    factors = [1]
    for prime, exponents in prime_factors(number).items():
        pfactors = [prime**i for i in range(1, exponents + 1)]
        factors += [i * factor for factor in factors for i in pfactors]
    return factors

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            number = int(input())
            difference = sum(distinct_factors(number)) - (number << 1)
            if difference:
                if difference in range(-2, 3):
                    print(number, 'almost perfect')
                else:
                    print(number, 'not perfect')
            else:
                print(number, 'perfect')
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
