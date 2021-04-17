'''
Convert English miles to Roman paces

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    paces = 5280000 * float(input()) / 4854
    result = int(paces)
    if paces - result >= 0.5:
        result += 1
    print(result)

###############################################################################

if __name__ == '__main__':
    main()
