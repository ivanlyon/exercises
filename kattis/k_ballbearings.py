'''
Maximimum number of bearings in confined space using law of cosines

Status: Accepted
'''

from math import pi, acos

###############################################################################

def main():
    """Read input and print output"""

    for _ in range(int(input())):
        diam_inner, diam_ball, gap = [float(i) for i in input().split()]
        side_near = 0.5 * (diam_inner - diam_ball)
        side_far = diam_ball + gap
        denominator = 2 * side_near * side_near
        numerator = denominator - side_far * side_far
        print(int(2 * pi / acos(numerator / denominator)))

###############################################################################

if __name__ == '__main__':
    main()
