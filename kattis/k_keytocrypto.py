'''
Decode via autokey cipher

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output cipher decoded with autokey"""

    ord_a = ord('A')
    ord_aa = ord_a << 1

    cipher = input()
    key = input()
    length = len(key)
    for index, glyph in enumerate(cipher):
        key += chr(ord_a + ((ord(glyph) - ord(key[index]) - ord_aa + 26) % 26))

    print(key[length:])

###############################################################################

if __name__ == '__main__':
    main()
