'''
Compute number of permutations containing specified number of descents

Status: Accepted
'''

def memoize(user_function):
    """Memoization decorator for user function of 1+ parameters"""

    class Memodict(dict):
        """Memoization performs user function call on dict miss"""

        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            result = self[key] = user_function(*key)
            return result

    return Memodict().__getitem__

###############################################################################

@memoize
def permutations(numbers, descents):
    """Compute number of permutations with specified number of descents"""

    if descents in (0, numbers - 1):
        return 1

    add0 = (descents + 1) * permutations(numbers - 1, descents)
    add1 = (numbers - descents) * permutations(numbers - 1, descents - 1)
    return (add0 + add1) % 1001113

###############################################################################

def main():
    """Read input and print output for descending permutations query"""

    for _ in range(int(input())):
        test_case, numbers, descents = [int(i) for i in input().split()]
        print(test_case, permutations(numbers, descents))

###############################################################################

if __name__ == '__main__':
    main()
