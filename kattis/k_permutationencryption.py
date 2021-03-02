'''
Perform permutation encryption

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        numbers = [(int(i) - 1) for i in input().split()]
        length = numbers[0] + 1
        if length:
            numbers = numbers[1:]
            text = input()
            filler = (length - (len(text) % length)) % length
            text = list(text + filler * ' ')
            result = list('*' * len(text))
            for step in range(0, len(text), length):
                for index in range(length):
                    result[step + index] = text[step + numbers[index]]
            print("'" + ''.join(result) + "'")
        else:
            break

###############################################################################

if __name__ == '__main__':
    main()
