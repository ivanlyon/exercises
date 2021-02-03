'''
Determine cost given a single variable function

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output cost of 3 entities generating costs"""

    cost_a, cost_b, cost_c = [int(i) for i in input().split()]
    parked = [0] * 102

    for _ in range(3):
        arrive, depart = [int(i) for i in input().split()]
        for i in range(arrive, depart):
            parked[i] += 1

    result = sum([1 for trucks in parked if trucks == 1]) * cost_a
    result += sum([2 for trucks in parked if trucks == 2]) * cost_b
    result += sum([3 for trucks in parked if trucks == 3]) * cost_c

    print(result)

###############################################################################

if __name__ == '__main__':
    main()
