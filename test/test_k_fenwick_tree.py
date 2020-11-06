import unittest
from kattis import k_fenwick_tree

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        tree1 = k_fenwick_tree.create_tree(10)
        k_fenwick_tree.change_value(tree1, 7, 23)
        self.assertEqual(tree1, [0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0])
        self.assertEqual(k_fenwick_tree.query_value(tree1, 8), 23)
        k_fenwick_tree.change_value(tree1, 3, 17)
        self.assertEqual(tree1, [0, 0, 0, 0, 17, 0, 0, 0, 40, 0, 0])
        self.assertEqual(k_fenwick_tree.query_value(tree1, 8), 40)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        tree2 = k_fenwick_tree.create_tree(5)
        k_fenwick_tree.change_value(tree2, 0, -43)
        self.assertEqual(tree2, [0, -43, -43, 0, -43, 0])
        k_fenwick_tree.change_value(tree2, 4, 1)
        self.assertEqual(tree2, [0, -43, -43, 0, -43, 1])
        self.assertEqual(k_fenwick_tree.query_value(tree2, 0), 0)
        self.assertEqual(k_fenwick_tree.query_value(tree2, 5), -42)

###############################################################################

if __name__ == '__main__':
    unittest.main()
