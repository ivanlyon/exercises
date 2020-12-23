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

    def flooded(self):
        '''Use to peek at intermediate results between queries'''
        results = []
        for _r in range(self._rows):
            for _c in range(self._columns):
                if isinstance(self._grid[_r][_c], int):
                    results.append((_r, _c))
        return results

    def glyph(self, row, col):
        '''Return the original text glyph of a flood-filled integer'''
        if self._onebase:
            row, col = (row - 1, col - 1)

        if isinstance(self._grid[row][col], int):
            return self._glyphs[self._grid[row][col]]
        return self._grid[row][col]

###############################################################################

def solver(matrix, queries, demonstration=False):
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

    if demonstration:
        demo_results = []
        ggrid = GraphGrid(grid=matrix, onebase=True)
        for query in queries:
            row1, col1, row2, col2 = query
            ggrid.connected(row1, col1, row2, col2)
            demo_results.append((solutions[len(demo_results)], ggrid.flooded()))
        return demo_results

    return solutions

###############################################################################

def main():
    '''Solver of one test case from stdin'''
    matrix = []
    query = []

    rows, _columns = [int(i) for i in stdin.readline().split()]
    for _ in range(rows):
        matrix.append(stdin.readline().strip())

    for _ in range(int(stdin.readline())):
        query.append([int(i) for i in stdin.readline().split()])

    for result in solver(matrix, query):
        print(result)

###############################################################################

def normalized_point(x_coord, y_coord, rows, columns):
    '''Function to translate table row and column to plot x, y coordinates'''
    x_new = (x_coord - 0.5) / columns
    y_new = 1 - (y_coord - 0.5) / rows
    return (x_new, y_new)

###############################################################################

def demo():
    '''Random input and queries for plot display'''
    import random
    import matplotlib.pyplot as plt
    from matplotlib import animation

    rows, columns = 20, 20 # Hard coded to make screen coordinates work
    query, matrix = [], []
    for _r in range(rows):
        matrix.append('')
        for _c in range(columns):
            matrix[-1] += random.choice('01')
        print(matrix[-1])

    pt1, pt2 = [], []
    for _ in range(random.randint(16, 20)):
        query.append([random.randint(1, rows),
                      random.randint(1, columns),
                      random.randint(1, rows),
                      random.randint(1, columns)])
        pt1.append(normalized_point(query[-1][1], query[-1][0], rows, columns))
        pt2.append(normalized_point(query[-1][3], query[-1][2], rows, columns))

    results = solver(matrix, query, True)

    # Prepending empty content to allow for 'clean slate' animation
    query, results = [[]] + query, [[]] + results
    pt1, pt2 = [[]] + pt1, [[]] + pt2

    assigned = {}
    flood_color = []
    for index, ptn in enumerate(query):
        if index:
            print('Query {:02d} {:02d} {:02d} {:02d} = '.format(ptn[0], ptn[1], ptn[2], ptn[3]) + results[index][0])
            for flooding in results[index][1]:
                if flooding not in assigned:
                    assigned[flooding] = index
            x_r = '123456789ABCDE'[int((ptn[1] - 1) * 13 / 19)]
            y_g = '123456789ABCDE'[int((ptn[0] - 1) * 13 / 19)]
            random_b = random.choice('123456789ABCDE')
            flood_color.append("#" + 2*x_r + 2*y_g + 2*random_b)
        else:
            flood_color.append("")

    _fig, axes = plt.subplots()
    plt.suptitle('10kindsofpeople Demonstration (Random Grid Values)')
    axes.axis('off')

    for row in matrix:
        row = list(row)
    table = plt.table(cellText=matrix, loc='center', cellLoc='center')
    table.scale(1, 1.1) # Kludge to make table coordinates align with plot area
    updating = [None]

    def animate(i):
        '''Show query results and flooding work'''
        if updating[0]:
            updating[0].remove()
        if i:
            updating[0] = axes.arrow(pt1[i][0], pt1[i][1],
                                     pt2[i][0] - pt1[i][0], pt2[i][1] - pt1[i][1],
                                     facecolor='red', edgecolor='red',
                                     head_width=.03, head_length=.03,
                                     length_includes_head=True)
            axes.title.set_text('Query {:d}: from '.format(i) + str(query[i][:2]) + '->' + str(query[i][2:]) + ' = ' + results[i][0])
            for flooding in results[i][1]:
                the_cell = table[flooding[0], flooding[1]]
                the_cell.set_facecolor(flood_color[assigned[flooding]])
        else:
            updating[0] = axes.arrow(0, 0, 0, 0, head_length=0, width=0)
            axes.title.set_text('')
            for the_cell in table.get_children():
                the_cell.set_facecolor('#FFFFFF')
        return updating

    _ = animation.FuncAnimation(_fig, animate, frames=len(query), interval=2000, blit=False)
    plt.show()

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="demonstration of queries and results", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
