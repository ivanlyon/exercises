'''
Expected result of ordered probability attempts

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    result, prob, words = 0.0, [], int(input())
    for _ in range(words):
        prob.append(float(input().split()[1]))

    for attempts, chance in enumerate(sorted(prob, reverse=True), start=1):
        result += attempts * chance

    print(result)

###############################################################################

if __name__ == '__main__':
    main()
