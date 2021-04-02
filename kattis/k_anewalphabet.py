'''
Replace text glyphs

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    translation = {}
    translation['a'] = '@'
    translation['b'] = '8'
    translation['c'] = '('
    translation['d'] = '|)'
    translation['e'] = '3'
    translation['f'] = '#'
    translation['g'] = '6'
    translation['h'] = '[-]'
    translation['i'] = '|'
    translation['j'] = '_|'
    translation['k'] = '|<'
    translation['l'] = '1'
    translation['m'] = '[]\\/[]'
    translation['n'] = '[]\\[]'
    translation['o'] = '0'
    translation['p'] = '|D'
    translation['q'] = '(,)'
    translation['r'] = '|Z'
    translation['s'] = '$'
    translation['t'] = "']['"
    translation['u'] = '|_|'
    translation['v'] = '\\/'
    translation['w'] = '\\/\\/'
    translation['x'] = '}{'
    translation['y'] = '`/'
    translation['z'] = '2'

    result = ''
    for glyph in input().lower():
        if glyph in translation:
            result += translation[glyph]
        else:
            result += glyph
    print(result)

###############################################################################

if __name__ == '__main__':
    main()
