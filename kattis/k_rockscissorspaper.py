'''
Deliver state of Rock-Paper-Scissors style of Conway game of life

Status: Accepted
'''

###############################################################################

class RockPaperScissorsGrid():
    '''Conway life-style grid'''

    def __init__(self, grid):
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0])

    def neighbors(self, row, col):
        "List valid neighbors for grid location"
        results = []
        if row > 0:
            results.append(self._grid[row - 1][col])
        if col > 0:
            results.append(self._grid[row][col - 1])
        if row < self._rows - 1:
            results.append(self._grid[row + 1][col])
        if col < self._cols - 1:
            results.append(self._grid[row][col + 1])
        return ''.join(results)

    def compete(self, days):
        "Perform all the changes resulting from competition over some days"
        trumped_by = {'S': 'R', 'P': 'S', 'R': 'P'}
        newline = [''] * self._cols
        for _ in range(days):
            newgrid = [''] * self._rows
            for row, text in enumerate(self._grid):
                for col, glyph in enumerate(text):
                    if trumped_by[glyph] in self.neighbors(row, col):
                        newline[col] = trumped_by[glyph]
                    else:
                        newline[col] = glyph
                newgrid[row] = ''.join(newline)
            self._grid = newgrid

    def __repr__(self):
        return '\n'.join(self._grid)

###############################################################################

def main():
    """Read input and print output"""

    for test_case in range(int(input())):
        if test_case:
            print()

        rows, _, days = [int(i) for i in input().split()]
        grid = []
        for _ in range(rows):
            grid.append(input())

        rpsg = RockPaperScissorsGrid(grid)
        rpsg.compete(days)
        print(rpsg)

###############################################################################

def demo():
    '''RPS animation over random grid'''

    import matplotlib.pyplot as plt
    from matplotlib import animation
    from random import choice

    # Test case data
    rows, columns = 20, 20
    matrix = []
    for _r in range(rows):
        matrix.append(''.join([choice('RRRRRPS') for _ in range(columns)]))
    days = 24

    # Console display
    rpsg = RockPaperScissorsGrid(matrix)
    print("Random input:")
    print(rpsg)
    print("\nDay", days, "Output:")
    rpsg.compete(days)
    print(rpsg)

    _fig, axes = plt.subplots()
    plt.suptitle('Rock-Paper-Scissors Demonstration (Random Grid)')
    axes.axis('off')

    rpsg2 = None
    bg_color = {'R': '#FFBBBB', 'P': '#BBFFBB', 'S': '#BBBBFF'}
    def animate(i):
        '''Show Rock Paper Scissors grid per day'''
        nonlocal rpsg2
        if i:
            rpsg2.compete(1)
        else:
            rpsg2 = RockPaperScissorsGrid(matrix)
        table = plt.table(cellText=rpsg2._grid, loc='center', cellLoc='center')

        axes.title.set_text('Day {:d}'.format(i))
        for the_cell in table.get_children():
            the_cell.set_facecolor(bg_color[the_cell.get_text().get_text()])

    _ = animation.FuncAnimation(_fig, animate, frames=days+1, interval=500, blit=False)
    plt.show()

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="demonstration of rock-paper-scissors", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
