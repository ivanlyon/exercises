'''
Interpret text as though all letters are off by one key location

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    lut, keys = {' ': ' '}, []
    keys.append('`1234567890-=')
    keys.append('QWERTYUIOP[]\\')
    keys.append('ASDFGHJKL;\'')
    keys.append('ZXCVBNM,./')

    for row in keys:
        for index, k in enumerate(row[1:], start=1):
            lut[k] = row[index - 1]

    while True:
        try:
            print(''.join([lut[i] for i in input()]))
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
