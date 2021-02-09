'''
Compute angle and velocity of a billiard style physics problem

Status: Accepted
'''

import math

###############################################################################

def main():
    """Read input and print output"""

    while True:
        horizontal, vertical, seconds, vbounces, hbounces = [int(i) for i in input().split()]
        if horizontal or vertical or seconds or vbounces or hbounces:
            horizontal *= vbounces
            vertical *= hbounces
            angle = math.degrees(math.atan(vertical / horizontal))
            velocity = math.sqrt(vertical * vertical + horizontal * horizontal) / seconds
            print('{0:.2f} {1:.2f}'.format(angle, velocity))
        else:
            break

###############################################################################

if __name__ == '__main__':
    main()
