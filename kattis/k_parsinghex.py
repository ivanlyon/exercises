'''
Find and translate hexadecimal numbers embedded in text

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output to find and print hex numbers"""

    hex_chars = '0123456789abcdefABCDEF'
    prefixes = ['0x', '0X']

    while True:
        try:
            text = input()
        except EOFError:
            break

        len_text = len(text)
        text += '$'
        for lhs in range(len_text):
            if text[lhs:lhs + 2] in prefixes:
                rhs = lhs + 2
                while text[rhs] in hex_chars:
                    rhs += 1
                if rhs > lhs + 2:
                    print(text[lhs:rhs], int(text[lhs:rhs], base=16))

###############################################################################

if __name__ == '__main__':
    main()
