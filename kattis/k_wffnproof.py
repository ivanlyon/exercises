'''
Produce longest WFF with provided inputs

Status: Accepted
'''

import argparse

###############################################################################

def longest_wff(text):
    '''Return greedy wff of longest length'''

    unary, binary, literal = [], [], []
    for glyph in text:
        if glyph in 'N':
            unary.append(glyph)
        if glyph in 'KACE':
            binary.append(glyph)
        if glyph in 'pqrst':
            literal.append(glyph)

    if literal:
        result = ''
        while binary and len(literal) > 1:
            result += binary.pop() + literal.pop()
        return result + 'N' * len(unary) + literal[0]

    return 'no WFF possible'

###############################################################################

def main():
    """Read input and print output"""

    while True:
        text = input().strip()
        if text == '0':
            break
        print(longest_wff(text))

###############################################################################

def demo():
    '''Demonstrate production of longest WFF using random input'''

    import random

    letters = 'KACENpqrst Xx'
    text = ''.join(random.choices(letters, k=random.randint(20, 25)))
    print("Given (dice?) input: '" + text + "'")
    print("One WFF of the longest length is: " + longest_wff(text))

###############################################################################

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="wff 'n proof", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
