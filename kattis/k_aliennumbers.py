'''
Translate number from one system to another

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output numbers in a designated number system"""

    test_cases = int(input().strip())
    for test_case in range(1, test_cases + 1):
        alien_number, source, target = input().strip().split()
        len_source, len_target = len(source), len(target)
        values = {}
        for index, glyph in enumerate(source):
            values[glyph] = index

        value = 0
        for glyph in alien_number:
            value = value * len_source + values[glyph]

        if value:
            result = ''
            while value:
                result = target[value % len_target] + result
                value //= len_target
        else:
            result = target[0]

        print('Case #{0}: {1}'.format(test_case, result))

###############################################################################

if __name__ == '__main__':
    main()
