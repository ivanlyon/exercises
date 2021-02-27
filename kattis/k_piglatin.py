'''
Translate text to pig latin

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    while True:
        try:
            text = input()
        except EOFError:
            break

        platin = []
        for word in text.split():
            if word[0] in 'aeiouy':
                platin.append(word + 'yay')
            else:
                index = -1
                for index, letter in enumerate(list(word)):
                    if letter in 'aeiouy':
                        break
                platin.append(word[index:] + word[:index] + 'ay')
        print(' '.join(platin))

###############################################################################

if __name__ == '__main__':
    main()
