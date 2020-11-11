'''
Kruskal's algorithm used to generate minimum spanning tree(s).

Status: Accepted
'''
import math
import sys

###############################################################################

def strongly_connect(locations):
    '''For input locations, use x, y coordinates to create edges from each
    point to all other points.  In this fashion, the set of points is modeled
    as a strongly connected graph weighted by distance.'''
    edges = []
    for u in range(len(locations)):
        x = locations[u][0]
        y = locations[u][1]
        for v in range(u):
            dx = x - locations[v][0]
            dy = y - locations[v][1]
            edges.append((u, v, math.sqrt(dx * dx + dy * dy)))

    return edges

###############################################################################

def kruskal(nodes, edges, number_to_link):
    '''Create minimum spanning tree(s) from a list of nodes and list of
    weighted edges.
    '''
    mst = []
    trees = [set([_]) for _ in range(nodes)]
    linked = 0

    for u, v, d in sorted(edges, key=lambda x: x[2]):
        for i in range(len(trees)):
            if u in trees[i]:
                uparent = i
            if v in trees[i]:
                vparent = i
        if uparent != vparent:
            mst.append((u, v, d))
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
        for u in range(outposts):
            locations.append([int(i) for i in input().split()])

        mst = kruskal(outposts, strongly_connect(locations),
                      outposts - satellites)

        print('Minimum distance to create {} trees: '.format(satellites),
              end='',
              flush=True,
              file=sys.stderr)

        print('{:.02f}'.format(mst[-1][2]))


###############################################################################
