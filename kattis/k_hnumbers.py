'''
Determine number of H-semi-primes between 1 and the input number

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output count of H-semi-primes"""

    limit = 1000002
    limit_root = 1002
    is_prime = [(i % 4 == 1) for i in range(limit)]
    is_prime[1] = False # Unit
    for index in range(5, limit_root, 4):
        if is_prime[index]:
            index4 = index << 2
            for jindex in range(index * index, limit, index4):
                is_prime[jindex] = False
    primes = [i for i in range(limit) if is_prime[i]]

    semis = [0] * limit
    for index, number in enumerate(primes):
        if number > limit_root:
            break

        other = index
        while number * primes[other] < limit:
            semis[number * primes[other]] = 1
            other += 1

    for index in range(24, limit):
        semis[index] += semis[index - 1]

    while True:
        number = int(input())
        if number:
            print(number, semis[number])
        else:
            break

###############################################################################

if __name__ == '__main__':
    main()
