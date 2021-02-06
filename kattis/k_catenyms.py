'''
Determine chain of words using complete set of input

Status: Accepted
'''
from sys import setrecursionlimit
from string import ascii_lowercase

setrecursionlimit(2048)
CATENYMS, MATRIX = None, None
LEN_WORDS = 0

###############################################################################

def start_end(in_degrees, out_degrees):
    """Determine the start and end nodes of a euler walk"""

    valid = True
    start, end = None, None
    for letter in ascii_lowercase:
        if in_degrees[letter] - out_degrees[letter] == 1:
            valid &= (end is None)
            end = letter
        elif out_degrees[letter] - in_degrees[letter] == 1:
            valid &= (start is None)
            start = letter
        elif out_degrees[letter] != in_degrees[letter]:
            valid = False

    if valid:
        if start:
            return start, end

        for letter in ascii_lowercase:
            if in_degrees[letter]:
                return letter, letter

    return None, None

###############################################################################

def dfs(location):
    """Determine longest possible path searching in lexicographic order"""

    global LEN_WORDS, MATRIX, CATENYMS

    if len(CATENYMS) == LEN_WORDS:
        return True

    for word in sorted(set(MATRIX[location])):
        MATRIX[location].remove(word)
        CATENYMS.append(word)
        if dfs(word[-1]):
            return True
        CATENYMS.pop()
        MATRIX[location].append(word)

    return False

###############################################################################

def euler_walk(words):
    """Return lexicographically least traversal of all words"""

    global LEN_WORDS, MATRIX, CATENYMS

    CATENYMS = []
    MATRIX, in_degree, out_degree = {}, {}, {}
    for first_letter in ascii_lowercase:
        out_degree[first_letter] = 0
        in_degree[first_letter] = 0
        MATRIX[first_letter] = []

    for word in words:
        in_degree[word[-1]] += 1
        out_degree[word[0]] += 1
        MATRIX[word[0]].append(word)

    start, end = start_end(in_degree, out_degree)
    if start and end:
        LEN_WORDS = len(words)
        if not dfs(start):
            CATENYMS = []

###############################################################################

def main():
    """Read input and print output for euler walk with words as edges"""

    global CATENYMS

    for _ in range(int(input().strip())):
        words = []
        for _ in range(int(input().strip())):
            words.append(input().strip())

        euler_walk(words)
        if CATENYMS:
            print('.'.join(CATENYMS))
        else:
            print('***')

###############################################################################

if __name__ == '__main__':
    main()
