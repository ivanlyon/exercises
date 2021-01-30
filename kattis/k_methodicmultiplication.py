'''
Print custom string depicting product of two peano numbers

Status: Accepted
'''

###############################################################################

def main():
    """Print a custom string depicting product of two input custom numbers"""

    number1 = len(input().strip()) // 3
    number2 = len(input().strip()) // 3
    product = number1 * number2

    print('S(' * product + '0' + ')' * product)

###############################################################################

if __name__ == '__main__':
    main()
