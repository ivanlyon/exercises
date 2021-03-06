'''
Minimal modifications to create palindrome

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        text = input()
        lhs, rhs = 0, len(text) - 1
        swaps, failures = 0, 0
        while failures < 2 and lhs < rhs:
            i = rhs
            while text[lhs] != text[i]:
                i -= 1

            if i > lhs:
                swaps += rhs - i
                text = text[:i] + text[i + 1:rhs + 1] + text[i] + text[rhs + 1:]
                lhs += 1
                rhs -= 1
            else:
                failures += 1
                text = ''.join(reversed(text))
        if failures < 2:
            print(swaps)
        else:
            print('Impossible')

###############################################################################

if __name__ == '__main__':
    main()
