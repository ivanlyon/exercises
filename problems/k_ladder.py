'''
Compute hypotenuse length given angle and opposite side length.
'''

import math

if __name__ == '__main__':
    length, angle = [int(i) for i in input().split()]
    print(math.ceil(length / math.sin(angle * math.pi / 180.0)))
