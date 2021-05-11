'''
Is there a way to create an sum of a few fixed numbers

Status: Accepted
'''

from collections import deque

###############################################################################

def main():
    """Read input and print output"""

    _ = input() # Read past unnecessary line
    angles = [int(i) for i in input().split()]
    for query in map(int, input().split()):
        the_q, located = deque([query]), set()
        while the_q:
            location = the_q.popleft()
            for angle in angles:
                guess = (location + angle) % 360
                if guess not in located:
                    located.add(guess)
                    the_q.append(guess)
                guess2 = (location - angle + 360) % 360
                if guess2 not in located:
                    located.add(guess2)
                    the_q.append(guess2)

        if 0 in located:
            print("YES")
        else:
            print("NO")

###############################################################################

if __name__ == '__main__':
    main()
