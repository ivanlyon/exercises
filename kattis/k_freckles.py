'''
Minimum spanning tree

Status: Accepted
'''

from math import sqrt
from heapq import heappop, heappush

###############################################################################

def main():
    """Read input and print output"""

    sqr = lambda a: a*a
    for _ in range(int(input())):
        if _:
            print() # print blank line between consecutive test cases
        _ = input() # read blank line before all test cases

        freckles, points = int(input()), []
        dist2_from_to = [[0.0]*freckles for _ in range(freckles)]
        for index1 in range(freckles):
            pt_x, pt_y = map(float, input().split())
            for index2, point2 in enumerate(points):
                dist2_from_to[index1][index2] = sqr(pt_x - point2[0]) + sqr(pt_y - point2[1])
                dist2_from_to[index2][index1] = dist2_from_to[index1][index2]
            points.append((pt_x, pt_y))

        arc_heap = []
        shortest2 = [-1.0] * freckles
        for index2 in range(freckles):
            heappush(arc_heap, (dist2_from_to[0][index2], index2))
            shortest2[index2] = dist2_from_to[0][index2]

        must_visit = set(range(1, freckles))
        result, index1 = 0.0, 0
        for points in range(1, freckles):
            while index1 not in must_visit:
                dist2, index1 = heappop(arc_heap)
            must_visit.remove(index1)
            result += sqrt(dist2)
            for index2 in must_visit:
                if shortest2[index2] >= dist2_from_to[index1][index2]:
                    shortest2[index2] = dist2_from_to[index1][index2]
                    heappush(arc_heap, (shortest2[index2], index2))

        print('{0:0.2f}'.format(result))

###############################################################################

if __name__ == '__main__':
    main()
