import unittest
from problems import k_catalan_numbers

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''

        self.assertEqual(k_catalan_numbers.catalan(1), 1)
        self.assertEqual(k_catalan_numbers.catalan(2), 2)
        self.assertEqual(k_catalan_numbers.catalan(3), 5)
        self.assertEqual(k_catalan_numbers.catalan(4), 14)
        self.assertEqual(k_catalan_numbers.catalan(5), 42)
        self.assertEqual(k_catalan_numbers.catalan(50), 1978261657756160653623774456)

###############################################################################

if __name__ == '__main__':
    unittest.main()
