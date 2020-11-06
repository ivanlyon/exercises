'''
Compute hypotenuse length given angle and opposite side length.
'''

import math

def compute_length(length, angle):
    '''Compute hypotenuse length'''
    return math.ceil(length / math.sin(angle * math.pi / 180.0))

if __name__ == '__main__':
    length, angle = [int(i) for i in input().split()]
    print(compute_length(length, angle))
