"""
XYZZY is a maze with cost per location.

Status: Accepted
"""

import sys
from collections import namedtuple

AdjCost = namedtuple('AdjCost', ['adj', 'cost'])

###############################################################################

def bellman_ford(adj_energy, source, sink):
    '''Perform flow and cycle detection'''

    _oo = 20000000000
    energy = [_oo for _ in range(sink + 1)]
    negative_cycle = [False for _ in range(sink + 1)]
    energy[source] = 0
    for _ in range(sink + 1):
        for room in range(sink + 1):
            if energy[room] < _oo:
                for edge in adj_energy[room]:
                    if energy[room] + edge.cost < 0:
                        energy[edge.adj] = min(energy[edge.adj],
                                               energy[room] + edge.cost)

    relaxing = True
    while relaxing:
        relaxing = False
        for room in range(sink + 1):
            if energy[room] != _oo:
                for edge in adj_energy[room]:
                    if energy[edge.adj] > energy[room] + edge.cost and \
                            not negative_cycle[edge.adj] and \
                            energy[room] + edge.cost < 0:
                        energy[edge.adj] = -_oo
                        relaxing = True
                        negative_cycle[edge.adj] = True

    return energy[sink]

###############################################################################

def _print_graph(graph):
    '''Utility to facilitate debugging'''

    for adj in graph:
        line = ''
        for edge in adj:
            line += ' ' + str(edge)
        print(line)

###############################################################################

def main():
    """Solve all testcases of XYZZY formatted input"""

    numbers = []
    for i in sys.stdin.read().splitlines():
        numbers += [int(k) for k in i.split()]

    index = 0
    energy_at_start = 100
    while numbers[index] != -1:
        rooms = numbers[index]
        index += 1
        room_cost = [0]
        graph = [[AdjCost(1, -energy_at_start)]] # contrived room 0
        for _ in range(rooms):
            room_cost.append(-numbers[index]) # inverted for Bellman Ford
            doors = numbers[index + 1]
            index += 2
            graph.append([AdjCost(i, 0) for i in numbers[index:index+doors] if i <= rooms])
            index += doors

        graph2 = []
        for adjacents in graph:
            graph2.append([])
            for edge in adjacents:
                graph2[-1].append(AdjCost(edge.adj, edge.cost + room_cost[edge.adj]))

        if bellman_ford(graph2, 0, rooms) < 0:
            print("winnable")
        else:
            print("hopeless")

###############################################################################

if __name__ == "__main__":
    main()
