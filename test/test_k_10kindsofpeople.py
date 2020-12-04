import unittest
from kattis import k_10kindsofpeople

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        matrix = ['1100']
        queries = []
        queries.append([1, 1, 1, 4])
        queries.append([1, 1, 1, 1])

        self.assertEqual(k_10kindsofpeople.solver(matrix, queries), ["neither", "decimal"])

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        matrix = []
        matrix.append('11111111111111111111')
        matrix.append('11000000000000000101')
        matrix.append('11111111111111110000')
        matrix.append('11111111111111110000')
        matrix.append('11000000000000000111')
        matrix.append('00011111111111111111')
        matrix.append('00111111111111111111')
        matrix.append('10000000000000001111')
        matrix.append('11111111111111111111')
        matrix.append('11111111111111111111')

        queries = []
        queries.append([2, 3, 8, 16])
        queries.append([8, 1, 7, 3])
        queries.append([1, 1, 10, 20])

        self.assertEqual(k_10kindsofpeople.solver(matrix, queries), ["binary", "decimal", "neither"])

    def test_for_rte(self):
        '''Attempt to reproduce the RTE caused during KATTIS test.'''
        matrix = []
        matrix.append('10')
        matrix.append('10')
        queries = []
        solutions = []
        queries.append([1, 1, 1, 1])
        queries.append([1, 1, 1, 2])
        queries.append([1, 1, 2, 1])
        queries.append([1, 1, 2, 2])
        solutions += ["decimal", "neither", "decimal", "neither"]
        queries.append([1, 2, 1, 1])
        queries.append([1, 2, 1, 2])
        queries.append([1, 2, 2, 1])
        queries.append([1, 2, 2, 2])
        solutions += ["neither", "binary", "neither", "binary"]
        queries.append([2, 1, 1, 1])
        queries.append([2, 1, 1, 2])
        queries.append([2, 1, 2, 1])
        queries.append([2, 1, 2, 2])
        solutions += ["decimal", "neither", "decimal", "neither"]
        queries.append([2, 2, 1, 1])
        queries.append([2, 2, 1, 2])
        queries.append([2, 2, 2, 1])
        queries.append([2, 2, 2, 2])
        solutions += ["neither", "binary", "neither", "binary"]

        self.assertEqual(k_10kindsofpeople.solver(matrix, queries), solutions)

###############################################################################

if __name__ == '__main__':
    unittest.main()
