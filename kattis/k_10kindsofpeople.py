'''
Determine if 2D grid graph nodes are connected.

Status: Accepted
'''

from sys import stdin

###############################################################################

class GraphGrid(object):
    '''Graph object of gridded nodes operations. Original node IDs are only
    accessible by method.'''
    def __init__(self, grid = None, onebase = False):
        if grid:
            self._grid = []
            for r in grid:
                self._grid.append(list(r))
        else:
            self._grid = None

        self._onebase = onebase
        self._floods = 0
        self._glyphs = '' # For preservation of node IDs removed by flood
        if self._grid:
            self._rows = len(self._grid)
            self._columns = len(self._grid[0])
        else:
            self._rows, self._columns = (0, 0)

    def _flood_fill(self, row, column):
        '''Replace connected node IDs with a flood fill value'''
        connecting = self._grid[row][column]
        DELTAS = ((0, 1), (1, 0), (-1, 0), (0, -1))
        self._grid[row][column] = self._floods
        flooding = [(row, column)]
        while flooding:
            r, c = flooding.pop()
            for delta in DELTAS:
                nr = r + delta[0]
                nc = c + delta[1]
                if (nr in range(self._rows)) and (nc in range(self._columns)):
                    if self._grid[nr][nc] == connecting:
                        self._grid[nr][nc] = self._floods
                        flooding.append((nr, nc))

        self._glyphs += connecting
        self._floods += 1

    def connected(self, r1, c1, r2, c2):
        '''Test if 2 nodes are connected'''
        if self._onebase:
            r1, c1, r2, c2 = [i - 1 for i in (r1, c1, r2, c2)]

        result = (type(self._grid[r1][c1]) == type(self._grid[r2][c2]))
        if result:
            if (type(self._grid[r1][c1]) != int):
                self._flood_fill(r1, c1)
            result = (self._grid[r1][c1] == self._grid[r2][c2])

        return result

    def glyph(self, r, c):
        '''Return the original text glyph of a flood-filled integer'''
        if self._onebase:
            r, c = (r - 1, c - 1)

        if type(self._grid[r][c]) == int:
            return self._glyphs[self._grid[r][c]]
        else:
            return self._grid[r][c]

###############################################################################

def solver(matrix, queries):
    '''Compute connection queries.'''

    RESULTS = {}
    RESULTS['0'] = 'binary'
    RESULTS['1'] = 'decimal'

    gg = GraphGrid(grid=matrix, onebase=True)
    result = []
    for query in queries:
        r1, c1, r2, c2 = query
        if gg.connected(r1, c1, r2, c2):
            result.append(RESULTS[gg.glyph(r1, c1)])
        else:
            result.append('neither')

    return result

###############################################################################

if __name__ == '__main__':
    matrix = []
    queries = []

    rows, columns = [int(i) for i in stdin.readline().split()]
    for r in range(rows):
        matrix.append(stdin.readline().strip())

    for query in range(int(stdin.readline())):
        queries.append([int(i) for i in stdin.readline().split()])

    for result in solver(matrix, queries):
        print(result)

###############################################################################
