'''
Determine if 2D grid graph nodes are connected.

Status: Accepted
'''

from sys import stdin

###############################################################################

class GraphGrid():
    '''Graph object of gridded nodes operations. Original node IDs are only
    accessible by method.'''
    def __init__(self, grid=None, onebase=False):
        if grid:
            self._grid = []
            for row in grid:
                self._grid.append(list(row))
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
        deltas = ((0, 1), (1, 0), (-1, 0), (0, -1))
        self._grid[row][column] = self._floods
        flooding = [(row, column)]
        while flooding:
            row, col = flooding.pop()
            for delta in deltas:
                nrow = row + delta[0]
                ncol = col + delta[1]
                if (nrow in range(self._rows)) and (ncol in range(self._columns)):
                    if self._grid[nrow][ncol] == connecting:
                        self._grid[nrow][ncol] = self._floods
                        flooding.append((nrow, ncol))

        self._glyphs += connecting
        self._floods += 1

    def connected(self, r1, c1, r2, c2):
        '''Test if 2 nodes are connected'''
        if self._onebase:
            r1, c1, r2, c2 = [i - 1 for i in (r1, c1, r2, c2)]

        matched = (type(self._grid[r1][c1]) == type(self._grid[r2][c2]))
        if matched:
            if not isinstance(self._grid[r1][c1], int):
                self._flood_fill(r1, c1)
            matched = (self._grid[r1][c1] == self._grid[r2][c2])

        return matched

    def glyph(self, row, col):
        '''Return the original text glyph of a flood-filled integer'''
        if self._onebase:
            row, col = (row - 1, col - 1)

        if isinstance(self._grid[row][col], int):
            return self._glyphs[self._grid[row][col]]
        return self._grid[row][col]

###############################################################################

def solver(matrix, queries):
    '''Compute connection queries.'''

    results = {}
    results['0'] = 'binary'
    results['1'] = 'decimal'

    ggrid = GraphGrid(grid=matrix, onebase=True)
    solutions = []
    for query in queries:
        row1, col1, row2, col2 = query
        if ggrid.connected(row1, col1, row2, col2):
            solutions.append(results[ggrid.glyph(row1, col1)])
        else:
            solutions.append('neither')

    return solutions

###############################################################################

if __name__ == '__main__':
    MATRIX = []
    QUERIES = []

    ROWS, COLUMNS = [int(i) for i in stdin.readline().split()]
    for _ in range(ROWS):
        MATRIX.append(stdin.readline().strip())

    for _ in range(int(stdin.readline())):
        QUERIES.append([int(i) for i in stdin.readline().split()])

    for result in solver(MATRIX, QUERIES):
        print(result)

###############################################################################
