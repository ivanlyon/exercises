'''
Display large font version of input times

Status: Accepted

'''

###############################################################################

def main():
    """Read input and print output"""

    lcd_glyphs = []
    lcd_glyphs.append('  +---+      +  +---+  +---+  +   +  +---+  +---+  +---+  +---+  +---+   ')
    lcd_glyphs.append('  |   |      |      |      |  |   |  |      |          |  |   |  |   |   ')
    lcd_glyphs.append('  |   |      |      |      |  |   |  |      |          |  |   |  |   |  o')
    lcd_glyphs.append('  +   +      +  +---+  +---+  +---+  +---+  +---+      +  +---+  +---+   ')
    lcd_glyphs.append('  |   |      |  |          |      |      |  |   |      |  |   |      |  o')
    lcd_glyphs.append('  |   |      |  |          |      |      |  |   |      |  |   |      |   ')
    lcd_glyphs.append('  +---+      +  +---+  +---+      +  +---+  +---+      +  +---+  +---+   ')

    text = None
    while True:
        if not text is None:
            print()
            print()

        text = input().strip()
        if text == 'end':
            print(text)
            break

        lcd_output = [''] * 7
        for glyph in text:
            if glyph == ':':
                offset = 70
            else:
                offset = int(glyph) * 7
            for index, lcds in enumerate(lcd_glyphs):
                lcd_output[index] += lcds[offset: offset + 7]

        for line in lcd_output:
            print(''.join(line)[2:])

###############################################################################

if __name__ == '__main__':
    main()
