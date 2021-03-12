'''
Modular arithmetic

Status: Accepted
'''

###############################################################################

def extended_gcd(a, b):
    """gcd(a, b), s, r such that a * s + b * r == gcd(a, b)"""

    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0

###############################################################################

def modinv(number, modulus):
    """Modular inverse works when number and modulus are coprime"""

    gcdenom, result, _ = extended_gcd(number % modulus, modulus)
    if gcdenom == 1:
        return result % modulus

    return None

###############################################################################

def main():
    """Read input and print output"""

    while True:
        modulus, operations = [int(i) for i in input().split()]
        if modulus == 0 and operations == 0:
            break

        for _ in range(operations):
            lhs, binop, rhs = input().split()
            lhs, rhs = int(lhs), int(rhs)
            if binop == '+':
                result = (lhs + rhs) % modulus
            elif binop == '-':
                result = (lhs - rhs + modulus) % modulus
            elif binop == '*':
                result = (lhs * rhs) % modulus
            else:
                mod_inv_rhs = modinv(rhs, modulus)
                if mod_inv_rhs:
                    result = (lhs * mod_inv_rhs) % modulus
                else:
                    result = -1
            print(result)

###############################################################################

if __name__ == '__main__':
    main()
