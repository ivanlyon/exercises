import unittest
from problems import k_arctic_network

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample input and output'''
    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        locations = [[0, 100], [0, 300], [0, 600], [150, 750]]
        edges = k_arctic_network.strongly_connect(locations)
        nodes = len(locations)
        mst = k_arctic_network.kruskal(nodes, edges, nodes - 2)

        self.assertGreater(mst[-1][2], 212.12)
        self.assertLess(   mst[-1][2], 212.14)

###############################################################################

class BoardInput(unittest.TestCase):
    '''UVA online judge forum sample input and output'''
    def test_board_input(self):
        '''Run and assert form sample input and output.'''
        locations = [[2414, 6028],
                     [1010, 1508],
                     [4244,  743],
                     [9021, 2690],
                     [1265, 5478],
                     [2918, 5462],
                     [3574, 8662],
                     [7098, 5207],
                     [4110, 2662],
                     [2624,  748],
                     [ 651, 5884],
                     [3873, 6556],
                     [8707,  397],
                     [7093, 3177],
                     [5930, 1904],
                     [2427, 3786],
                     [5994, 7001],
                     [1636, 5094],
                     [7332, 5012],
                     [6034, 1258],
                     [2405, 7364],
                     [8292,  983],
                     [5241, 7012]]
        edges = k_arctic_network.strongly_connect(locations)
        nodes = len(locations)
        mst = k_arctic_network.kruskal(nodes, edges, nodes - 4)

        self.assertGreater(mst[-1][2], 1862.60)
        self.assertLess(   mst[-1][2], 1862.62)

###############################################################################

if __name__ == '__main__':
    unittest.main()
