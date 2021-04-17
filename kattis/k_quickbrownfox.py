'''
Report letters missing from total set

Status: Accepted
'''

import string

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        used = set()
        for glyph in input().lower():
            if glyph in string.ascii_lowercase:
                used.add(glyph)

        if len(used) == 26:
            print('pangram')
        else:
            letters = ''
            for glyph in string.ascii_lowercase:
                if glyph not in used:
                    letters += glyph
            print('missing', letters)

###############################################################################

if __name__ == '__main__':
    main()
