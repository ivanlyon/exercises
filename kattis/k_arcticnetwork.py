'''
Kruskal's algorithm used to generate minimum spanning tree(s).

Status: Accepted
'''
import math
import sys

###############################################################################

def strongly_connect(positions):
    '''For input locations, use x, y coordinates to create edges from each
    point to all other points.  In this fashion, the set of points is modeled
    as a strongly connected graph weighted by distance.'''
    edges = []
    for pt1 in range(len(positions)):
        x_coord = positions[pt1][0]
        y_coord = positions[pt1][1]
        for pt2 in range(pt1):
            dx = x_coord - positions[pt2][0]
            dy = y_coord - positions[pt2][1]
            edges.append((pt1, pt2, math.sqrt(dx * dx + dy * dy)))

    return edges

###############################################################################

def kruskal(nodes, edges, number_to_link):
    '''Create minimum spanning tree(s) from a list of nodes and list of
    weighted edges.
    '''
    mst = []
    trees = [set([_]) for _ in range(nodes)]
    linked = 0

    for pt1, pt2, distance in sorted(edges, key=lambda x: x[2]):
        for i in range(len(trees)):
            if pt1 in trees[i]:
                uparent = i
            if pt2 in trees[i]:
                vparent = i
        if uparent != vparent:
            mst.append((pt1, pt2, distance))
            linked += 1
            if linked == number_to_link:
                break
            trees[uparent] = trees[uparent].union(trees[vparent])
            del trees[vparent]

    return mst

###############################################################################

if __name__ == '__main__':
    STDERROR_HEADER = \
    '''
    +------------------------------------------------------------------------+
    | If stderr is displayed and out of sync, then all below is stderr.      |
    +------------------------------------------------------------------------+
    '''
    print(STDERROR_HEADER, file=sys.stderr)

    for testcase in range(int(input())):
        satellites, outposts = [int(i) for i in input().split()]

        locations = []
        for _ in range(outposts):
            locations.append([int(i) for i in input().split()])

        mstree = kruskal(outposts, strongly_connect(locations),
                         outposts - satellites)

        print('Minimum distance to create {} trees: '.format(satellites),
              end='',
              flush=True,
              file=sys.stderr)

        print('{:.02f}'.format(mstree[-1][2]))


###############################################################################
