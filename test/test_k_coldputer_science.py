import unittest
from problems import k_coldputer_science

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        result = k_coldputer_science.count_negatives((5, -10, 15))
        self.assertEqual(result, 1)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        result = k_coldputer_science.count_negatives((-14, -5, -39, -5, -7))
        self.assertEqual(result, 5)

###############################################################################

class OtherInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_zero_result(self):
        '''Run and assert list of all non-negative numbers returns zero.'''

        result = k_coldputer_science.count_negatives((0, 5, 10, 15))
        self.assertEqual(result, 0)

    def test_empty_list(self):
        '''Run and assert empty list produces count of zero.'''

        result = k_coldputer_science.count_negatives(())
        self.assertEqual(result, 0)

###############################################################################

if __name__ == '__main__':
    unittest.main()
