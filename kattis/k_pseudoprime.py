'''
Detect pseudoprime aspect of number

Status: Accepted
'''

from math import gcd

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

def is_prime(number):
    """Return True if number is prime"""

    if number & 1 == 0:
        term = 2
    elif number % 3 == 0:
        term = 3
    else:
        term = pollard_rho(number)

    return number == term

###############################################################################

def main():
    """Read input and print output"""

    while True:
        p_num, a_num = [int(i) for i in input().split()]
        if p_num == 0 and a_num == 0:
            break

        result = (a_num == pow(a_num, p_num, p_num))
        if result:
            result = not is_prime(p_num)

        if result:
            print('yes')
        else:
            print('no')

###############################################################################

if __name__ == '__main__':
    main()
