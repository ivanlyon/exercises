'''
Determine reversed binary number of a decimal number

Status: Accepted
'''

###############################################################################

def main():
    """Read decimal number and output its reversed binary counterpart"""

    decimal = int(input().strip())
    binary_text = '{:b}'.format(decimal)
    print(str(int(binary_text[::-1], base=2)))

###############################################################################

if __name__ == '__main__':
    main()
