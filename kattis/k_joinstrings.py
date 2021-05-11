'''
Concatenate strings in specific order

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    number = int(input()) + 1
    words, adjacent, distant = [''] * number, list(range(number)), list(range(number))
    for i in range(1, number):
        words[i] = input()
    index_sum = number * (number - 1) // 2
    for _ in range(number - 2):
        i, j = [int(_) for _ in input().split()]
        adjacent[distant[i]] = j
        distant[i] = distant[j]
        index_sum -= j

    result = []
    while index_sum != adjacent[index_sum]:
        result.append(words[index_sum])
        index_sum = adjacent[index_sum]
    result.append(words[index_sum])
    print(''.join(result))

###############################################################################

if __name__ == '__main__':
    main()
