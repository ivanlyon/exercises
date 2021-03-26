'''
Table look up

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    lut = {}
    while True:
        text = input().split()
        if text:
            lut[text[1]] = text[0]
        else:
            break

    while True:
        try:
            text = input()
            if text in lut:
                print(lut[text])
            else:
                print('eh')
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
