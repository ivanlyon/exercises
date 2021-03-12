'''
Print text after interpreting '<' as backspace

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    result = []
    for i in input():
        if i == '<':
            if result:
                result.pop()
        else:
            result.append(i)
    print(''.join(result))

###############################################################################

if __name__ == '__main__':
    main()
