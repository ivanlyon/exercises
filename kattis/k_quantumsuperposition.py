"""
Graph DFS for steps to the largest numbered node.

Status: Time Limit Exceeded
"""

###############################################################################

def toposort(graph, nodes):
    """Topological sort-styled traversal of graph with counting of steps"""
    memo = set()
    indegree = [0 for _ in range(nodes + 1)]
    for adj in graph:
        for dest in adj:
            indegree[dest] += 1

    memo.add((1, 0))
    zero_degree = [1]
    while zero_degree:
        new_memos = set()
        node = zero_degree.pop()
        for edge in graph[node]:
            for seen in memo:
                if node == seen[0]:
                    new_memos.add((edge, seen[1] + 1))
            indegree[edge] -= 1
            if indegree[edge] == 0:
                zero_degree.append(edge)
        memo = memo.union(new_memos)

    return {r[1] for r in memo if r[0] == nodes}

###############################################################################

def main():
    """IO and top level calls for solution"""
    nodes1, nodes2, edges1, edges2 = [int(_) for _ in input().split()]
    graph1 = [[] for _ in range(nodes1 + 1)]
    graph2 = [[] for _ in range(nodes2 + 1)]
    for _ in range(edges1):
        _u, _v = [int(i) for i in input().split()]
        graph1[_u].append(_v)
    for _ in range(edges2):
        _u, _v = [int(i) for i in input().split()]
        graph2[_u].append(_v)

    steps1 = toposort(graph1, nodes1)
    steps2 = toposort(graph2, nodes2)

    totals = set()
    for steps1 in toposort(graph1, nodes1):
        for steps2 in toposort(graph2, nodes2):
            totals.add(steps1 + steps2)

    for _ in range(int(input())):
        if int(input()) in totals:
            print("Yes")
        else:
            print("No")

###############################################################################

if __name__ == "__main__":
    main()
