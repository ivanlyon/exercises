'''
Change order of letters in plain text

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        plain_text = list(input())
        length = len(plain_text)
        for root in range(102):
            if root * root >= length:
                break
        plain_text += ['*'] * (root * root - length)

        after = [''] * (root * root)
        for row in range(root):
            for col in range(root):
                after[col * root + (root - row - 1)] = plain_text[row * root + col]

        print(''.join(after).replace('*', ''))

###############################################################################

if __name__ == '__main__':
    main()
