'''
Compute soundex value of text input

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            text = input()
            result = '0'
            for glyph in text:
                if glyph in 'BFPV':
                    if result[-1] != '1':
                        result += '1'
                elif glyph in 'CGJKQSXZ':
                    if result[-1] != '2':
                        result += '2'
                elif glyph in 'DT':
                    if result[-1] != '3':
                        result += '3'
                elif glyph in 'L':
                    if result[-1] != '4':
                        result += '4'
                elif glyph in 'MN':
                    if result[-1] != '5':
                        result += '5'
                elif glyph in 'R':
                    if result[-1] != '6':
                        result += '6'
                else:
                    result += '0'
            print(result.replace('0', ''))
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
