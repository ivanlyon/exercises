'''
Determine both scores of a programming contest team

Status: Accepted
'''

from collections import Counter

###############################################################################

def main():
    """Read input and print output"""

    word_count, classification, sums = Counter(), {}, Counter()
    for _ in range(int(input())):
        text = input().split()
        classification[text[0]] = text[2:]
        for word in text[2:]:
            word_count[word] = 1

    while True:
        try:
            for word in input().split():
                if word in word_count:
                    word_count[word] += 1
        except EOFError:
            break

    for word in classification:
        for counting in classification[word]:
            sums[word] += word_count[counting]

    results = []
    max_freq = sums.most_common(1)[0][1]
    for word in sums:
        if sums[word] == max_freq:
            results.append(word)

    print('\n'.join(sorted(results)))

###############################################################################

if __name__ == '__main__':
    main()
