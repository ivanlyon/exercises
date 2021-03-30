'''
Determine winner of multiplication game based on factors

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

    if number & 1 == 0:
        term = 2
    elif number % 3 == 0:
        term = 3
    else:
        term = pollard_rho(number)

    if number == term:
        return Counter([number])

    return prime_factors(term) + prime_factors(number // term)

###############################################################################

def main():
    """Read input and print output"""

    results = ['Alice', 'Bob', 'tie']

    for _ in range(int(input())):
        number, first = input().split()
        result = 0 if first == 'Alice' else 1
        factors = prime_factors(int(number))
        if len(factors) == 1:
            _1, times = factors.popitem()
            result = (result + times + 1) % 2
        elif len(factors) == 2:
            _1, times1 = factors.popitem()
            _1, times2 = factors.popitem()
            if abs(times1 - times2) == 0:
                result = 1 - result
            elif abs(times1 - times2) > 1:
                result = 2
        else:
            result = 2

        print(results[result])

###############################################################################

if __name__ == '__main__':
    main()
