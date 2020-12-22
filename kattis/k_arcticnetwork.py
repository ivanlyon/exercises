'''
Kruskal's algorithm used to generate minimum spanning tree(s).

Status: Accepted
'''
import math

###############################################################################

def strongly_connect(positions):
    '''For input locations, use x, y coordinates to create edges from each
    point to all other points.  In this fashion, the set of points is modeled
    as a strongly connected graph weighted by distance.'''
    edges = []
    for index1, pt1 in enumerate(positions):
        x_coord = pt1[0]
        y_coord = pt1[1]
        for index2 in range(index1):
            d_x = x_coord - positions[index2][0]
            d_y = y_coord - positions[index2][1]
            edges.append((index1, index2, math.sqrt(d_x * d_x + d_y * d_y)))

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
        for index, branch in enumerate(trees):
            if pt1 in branch:
                uparent = index
            if pt2 in branch:
                vparent = index
        if uparent != vparent:
            mst.append((pt1, pt2, distance))
            linked += 1
            if linked == number_to_link:
                break
            trees[uparent] = trees[uparent].union(trees[vparent])
            del trees[vparent]

    return mst

###############################################################################

def main():
    '''Solve all testcases via formatted stdin content'''
    for _testcase in range(int(input())):
        satellites, outposts = [int(i) for i in input().split()]

        locations = []
        for _ in range(outposts):
            locations.append([int(i) for i in input().split()])

        mstree = kruskal(outposts, strongly_connect(locations),
                         outposts - satellites)

        print('{:.02f}'.format(mstree[-1][2]))

###############################################################################

def demo():
    '''Modified Kruskal algorithm demonstration with random points'''
    import matplotlib.pyplot as plt
    import random

    locations = []
    satellites = random.randint(2, 5)
    outposts = random.randint(10, 20)
    for _ in range(outposts):
        locations.append([random.randint(0, 1000), random.randint(0, 1000)])

    mstree = kruskal(outposts, strongly_connect(locations),
                     outposts - satellites)
    print('Minimal max arc cost when connecting {:d} outposts to {:d} satellites = {:.02f}'.format(outposts, satellites, mstree[-1][2]))
    for index, branch in enumerate(mstree, start=1):
        print(str(index) + ': ' + str(branch))

    fig, axes = plt.subplots()
    fig.set_facecolor('#eeffee')
    plt.suptitle('Arctic Network Demonstration (' + str(outposts) + ' random points)')
    axes.title.set_text('Minimal arc distance connecting outposts to {:d} satellites = {:.2f}'.format(satellites, mstree[-1][2]))
    axes.set_xlabel('X Coordinates')
    axes.set_ylabel('Y Coordinates')
    axes.plot([x[0] for x in locations], [y[1] for y in locations], color='red', marker='D', linewidth=0)
    for branch in mstree:
        x_coords = [locations[branch[0]][0], locations[branch[1]][0]]
        y_coords = [locations[branch[0]][1], locations[branch[1]][1]]
        axes.plot(x_coords, y_coords, color='green', marker='o')

    for index, ponte in enumerate(locations):
        axes.text(ponte[0]-40, ponte[1]-40, str(index))

    plt.show()

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="interval cover demonstration", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
