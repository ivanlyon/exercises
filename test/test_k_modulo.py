import unittest
from kattis import k_modulo
from collections import defaultdict

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        result = defaultdict(int)
        inputs = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        for i in inputs:
            result[i] += 1
        self.assertEqual(k_modulo.partition_dict(inputs), result)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        result = defaultdict(int)
        inputs = (39, 40, 41, 42, 43, 44, 82, 83, 84, 85)
        for i in inputs:
            result[i % 42] += 1
        self.assertEqual(k_modulo.partition_dict(inputs), result)

###############################################################################

if __name__ == '__main__':
    unittest.main()
