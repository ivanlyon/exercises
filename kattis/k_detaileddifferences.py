'''
Callout differences between 2 strings of same length

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        text1, text2, text3 = input(), input(), ''
        for glyph1, glyph2 in zip(text1, text2):
            if glyph1 == glyph2:
                text3 += '.'
            else:
                text3 += '*'
        print('\n'.join([text1, text2, text3, '']))

###############################################################################

if __name__ == '__main__':
    main()
