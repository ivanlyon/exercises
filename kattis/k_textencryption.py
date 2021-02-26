'''
Encode text with transposition cipher

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        decoder = int(input())
        if decoder == 0:
            break

        text = input().upper().replace(' ', '')
        text_length = len(text)
        encoded = [''] * text_length
        index, cycles = 0, 0
        for letter in list(text):
            encoded[index] = letter
            index += decoder
            if index >= text_length:
                cycles += 1
                index = cycles
        print(''.join(encoded))

###############################################################################

if __name__ == '__main__':
    main()
