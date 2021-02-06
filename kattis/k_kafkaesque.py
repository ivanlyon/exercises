'''
Determine number of ascending sequences starting from first available number

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output number of proper ascending sequences"""

    numbers = [int(input()) for _ in range(int(input()))]
    numbers.append(0)
    circuit, lhs = 0, 0
    while numbers[lhs]:
        while numbers[lhs] < numbers[lhs + 1]:
            lhs += 1
        lhs += 1
        circuit += 1
    print(circuit)

###############################################################################

if __name__ == '__main__':
    main()
