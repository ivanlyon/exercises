'''
Custom sorting

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    print_blank_line = False
    while True:
        rows, cols = [int(i) for i in input().split()]
        if rows + cols == 0:
            break

        if print_blank_line:
            print()
        print_blank_line = True

        words, results = [''] * cols, [''] * rows
        for _ in range(rows):
            for index, glyph in enumerate(input()):
                words[index] += glyph

        words.sort(key=str.lower)
        for word in words:
            for index, glyph in enumerate(word):
                results[index] += glyph

        print('\n'.join(results))

###############################################################################

if __name__ == '__main__':
    main()
