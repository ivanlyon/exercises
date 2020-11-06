import unittest
from kattis import k_catalan_numbers

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertEqual(k_catalan_numbers.catalan(4), 14)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        self.assertEqual(k_catalan_numbers.catalan(5), 42)

###############################################################################

if __name__ == '__main__':
    unittest.main()
