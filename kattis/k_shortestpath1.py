"""
Single source shortest path non-negative weight - so dijkstra's.

Status: Accepted
"""

import heapq
from collections import namedtuple

CostNode = namedtuple('CostNode', ['cost', 'node'])
CostEdge = namedtuple('CostEdge', ['cost', 'node', 'node2'])

###############################################################################

def main():
    """Solve all testcases of SSSP formatted input"""

    unset = -1
    while True:
        nodes, edges, queries, start = [int(i) for i in input().split()]
        if not (nodes or edges or queries or start):
            break

        cost_from_start = [unset for _ in range(nodes)]
        graph = [[] for _ in range(nodes)]
        for _ in range(edges):
            nfrom, nto, cost = [int(i) for i in input().split()]
            graph[nfrom].append(CostNode(cost, nto))

        hlist = []
        heapq.heappush(hlist, CostNode(0, start))
        while hlist:
            reaching = heapq.heappop(hlist)
            if cost_from_start[reaching.node] == unset:
                cost_from_start[reaching.node] = reaching.cost
                for edge in graph[reaching.node]:
                    if cost_from_start[edge.node] == unset:
                        heapq.heappush(hlist, CostNode(edge.cost + reaching.cost, edge.node))

        for _ in range(queries):
            query = int(input())
            if cost_from_start[query] == unset:
                print("Impossible")
            else:
                print(str(cost_from_start[query]))
        print()

###############################################################################

def dijkstra(graph_dict, start_node, total_nodes):
    '''Single Source Shortest Path computation'''
    unset = -1
    cost_from_start = {n:unset for n in total_nodes}

    graph = {}
    for node in total_nodes:
        graph[node] = []
    for edge in graph_dict:
        graph[edge[0]].append(CostEdge(graph_dict[edge], edge[0], edge[1]))

    hlist = []
    results = []
    heapq.heappush(hlist, CostEdge(0, start_node, start_node))
    while hlist:
        reaching = heapq.heappop(hlist)
        if cost_from_start[reaching.node2] == unset:
            cost_from_start[reaching.node2] = reaching.cost
            results.append(reaching)
            for edge in graph[reaching.node2]:
                if cost_from_start[edge.node2] == unset:
                    heapq.heappush(hlist, CostEdge(edge.cost + reaching.cost,\
                                   edge.node, edge.node2))
    return results

###############################################################################

def demo_tree(sssp, start_node):
    '''Create inorder traversal of tree to allow drawing with one plot command'''
    adjacents = {}
    for arc in sssp:
        if arc.cost > 0:
            if arc.node not in adjacents:
                adjacents[arc.node] = []
            adjacents[arc.node].append(CostNode(cost=arc.cost, node=arc.node2))

    def traversal(adjacents, pair):
        '''Inorder traversal of results for creation of drawable tree'''
        result = [pair]
        if pair in adjacents:
            for down in adjacents[pair]:
                result += traversal(adjacents, down.node)
                result.append(pair)
        return result

    return traversal(adjacents, start_node)

###############################################################################

def demo_plot(tree, adds, adds2, costs, nodes):
    '''Render plot of dijkstra result'''
    import matplotlib.pyplot as plt
    from matplotlib import animation

    xinorder = [i[0] for i in tree]
    yinorder = [i[1] for i in tree]

    fig, axes = plt.subplots(facecolor='#e5e5ff')
    plt.suptitle('Dijkstra Demonstration (' + str(len(nodes)) + ' random nodes)')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_xlim(-110, 110)
    axes.set_ylim(-110, 110)
    axes.set_facecolor('#eeffee')
    axes.plot(xinorder, yinorder, marker='D', linewidth=0, color='green')
    axes.plot(adds[0][0], adds[0][1], marker='D', color='red', zorder=4)
    axes.plot(xinorder, yinorder, color='gray', linestyle='dashed')
    legend = axes.text(.02, .945, "Initial String", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
                       transform=axes.transAxes, ha="left")

    lut = {}
    for index, ponte in enumerate(nodes):
        plt.text(ponte[0]-8, ponte[1]-8, str(index + 1))
        lut[ponte] = index + 1

    def animate(i):
        '''Draw one line segment per update'''
        pt1, pt2 = adds[i], adds2[i]
        if updating[0]:
            updating[0].remove()
        updating[0] = axes.arrow(pt1[0], pt1[1], pt2[0] - pt1[0], pt2[1] - pt1[1],
                                 facecolor='blue', edgecolor='blue',
                                 head_width=8, head_length=8, zorder=5,
                                 length_includes_head=True)
        axes.title.set_text('Cost from single source {:d} (Red) to node {:02d} = {:d}'.format(lut[adds[0]], lut[adds2[i]], costs[i]))
        legend.set_text('Step {:02d}: updating '.format(i) + str(adds[i]) +
                        '->' + str(adds2[i]) +
                        ' with total cost ' + str(costs[i]))
        return updating, legend

    updating = [None]
    anim = animation.FuncAnimation(fig, animate, frames=len(adds), interval=1000, blit=False)
    plt.show()

###############################################################################

def demo():
    '''Dijkstra demonstration with plotted paths.'''
    import random
    import math
    import pprint

    nodes = []
    lo_val = -100
    hi_val = 100
    random_points = random.randint(11, 18)
    for _ in range(random_points):
        while True:
            maybex = random.randint(lo_val, hi_val)
            maybey = random.randint(lo_val, hi_val)
            too_close = False
            for node in nodes:
                if abs(maybex - node[0]) < 10 and abs(maybey - node[1]) < 10:
                    too_close = True
            if not too_close:
                nodes.append((maybex, maybey))
                break
    start = random.randint(0, len(nodes) - 1)
    graph = {}
    for node in nodes:
        for node2 in nodes:
            xdiff = node[0] - node2[0]
            ydiff = node[1] - node2[1]
            graph[(node, node2)] = 1 + int(math.sqrt(xdiff * xdiff + ydiff * ydiff))
            graph[(node, node2)] *= random.randint(1, 4)
    sssp = dijkstra(graph, nodes[start], nodes)
    for arc in sssp:
        pprint.pprint(arc)

    inorder = demo_tree(sssp, nodes[start])
    demo_plot(inorder, [i.node for i in sssp], [i.node2 for i in sssp], \
              [i.cost for i in sssp], nodes)

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="dijkstra demonstration", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
