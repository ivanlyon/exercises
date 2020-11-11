import unittest
from exercises import knapsack

###############################################################################

class TestKnapsack(unittest.TestCase):
    '''
    Unittest class for the testing of a knapsack algorithm implementation.
    '''

    def test_empty_items(self):
        '''Test empty input to knapsack function.'''
        self.assertEqual(knapsack.knapsack([], 0), [])

    def test_1_item(self):
        '''Test single item inputs to knapsack function.'''
        self.assertEqual(knapsack.knapsack([[1, 2]], 2), [0])
        self.assertEqual(knapsack.knapsack([[1, 2]], 1), [])

    def test_n_items(self):
        '''Test multi-item inputs to knapsack function.'''
        items = []
        items.append([21, 10])
        items.append([43, 22])
        items.append([55, 26])
        items.append([80, 40])
        items.append([38, 20])
        items.append([18, 8])
        items.append([100, 51])
        items.append([62, 33])
        self.assertEqual(knapsack.knapsack(items, 111), [0, 1, 4, 5, 6])
        self.assertEqual(knapsack.knapsack(items, 112), [0, 1, 4, 5, 6])
        self.assertEqual(knapsack.knapsack(items, 113), [0, 1, 3, 5, 7])

###############################################################################

if __name__ == '__main__':
    unittest.main()
