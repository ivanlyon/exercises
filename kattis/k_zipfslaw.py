'''
Find words appearing a fixed number of times per test case

Status: Accepted
'''

from collections import Counter

###############################################################################

def alpha_only(text):
    '''Create list of words identified as only containing alpha characters'''

    splitters = {i for i in list(text) if not i.isalpha()}
    for splitter in splitters:
        text = ' '.join(text.split(splitter))
    return text.lower().split()

###############################################################################

def main():
    """Read input and print output"""

    text = None
    while True:
        try:
            frequency = int(input())
        except EOFError:
            break

        if not text is None:
            print()

        appearances = Counter()
        text = input().strip()
        while text != 'EndOfText':
            for word in alpha_only(text):
                appearances[word] += 1
            text = input()

        results = [i for i in appearances if appearances[i] == frequency]
        if results:
            print('\n'.join(sorted(results)))
        else:
            print('There is no such word.')

###############################################################################

if __name__ == '__main__':
    main()
