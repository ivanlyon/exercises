'''
Within a string locate matches of a substring

Status: Accepted
'''

###############################################################################

def kmp(pattern, text):
    """Knuth-Morris-Pratt substring matching"""

    pattern_length = len(pattern)
    matched, subpattern = 0, [0] * pattern_length
    for i, glyph in enumerate(pattern):
        if i:
            while matched and (pattern[matched] != glyph):
                matched = subpattern[matched - 1]
            matched += (pattern[matched] == glyph)
            subpattern[i] = matched

    matched, results = 0, []
    for i, glyph in enumerate(text):
        while matched and pattern[matched] != glyph:
            matched = subpattern[matched - 1]
        matched += (pattern[matched] == glyph)
        if matched == pattern_length:
            results.append(i + 1 - matched)
            matched = subpattern[matched - 1]

    return results

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            print(' '.join(map(str, kmp(input(), input()))))
        except EOFError:
            break

###############################################################################

if __name__ == '__main__':
    main()
