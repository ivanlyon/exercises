'''
Reverse rotation of text

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    index = {}
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    for i, letter in enumerate(letters):
        index[letter] = i

    while True:
        data = input()
        if data == '0':
            break

        rotate, plain_text = data.split()
        result, rotate = '', int(rotate)
        for letter in plain_text:
            result = letters[(index[letter] + rotate) % len(letters)] + result
        print(result)

###############################################################################

if __name__ == '__main__':
    main()
