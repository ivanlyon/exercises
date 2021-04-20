'''
Shortest repeating substring

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        text, repeat = input(), ''
        for glyph in text:
            repeat += glyph
            repeats = 1 + len(text) // len(repeat)
            if text == (repeat * repeats)[:len(text)]:
                break
        print(len(repeat))

###############################################################################

if __name__ == '__main__':
    main()
