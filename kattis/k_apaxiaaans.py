'''
No problem, just process

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    result = ''
    for i in input():
        if result:
            if i != result[-1]:
                result += i
        else:
            result = i
    print(result)

###############################################################################

if __name__ == '__main__':
    main()
