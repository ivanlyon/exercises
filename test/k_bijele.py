import unittest
from problems import k_catalan_numbers

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertEqual(k_bijele.get_difference((0, 1, 2, 2, 2, 7)), '1 0 0 0 0 1')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        self.assertEqual(k_bijele.get_difference((2, 1, 2, 1, 2, 1)), '-1 0 0 1 0 7')

###############################################################################

if __name__ == '__main__':
    unittest.main()
