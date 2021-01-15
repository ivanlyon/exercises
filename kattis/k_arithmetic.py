'''
Determine hex value of octal input number

Status: Accepted
'''

###############################################################################

def main():
    """Read an octal number and print the value in hex"""

    octal_text = input().strip()
    value = int(octal_text, base=8)
    print("{:X}".format(value))

###############################################################################

if __name__ == '__main__':
    main()
