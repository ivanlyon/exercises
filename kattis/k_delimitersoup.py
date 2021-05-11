'''
Static error detection

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    length, lhs, error = int(input()), [], False
    for index, glyph in enumerate(input() + ' '):
        if index == length:
            print('ok so far')
            break

        if glyph in '([{':
            lhs.append(glyph)
        elif glyph in ')]}':
            if len(lhs) == 0:
                error = True
            elif glyph == ')':
                error = (lhs[-1] != '(')
            elif glyph == ']':
                error = (lhs[-1] != '[')
            elif glyph == '}':
                error = (lhs[-1] != '{')

            if not error:
                lhs.pop()

        if error:
            print(glyph, index)
            break

###############################################################################

if __name__ == '__main__':
    main()
