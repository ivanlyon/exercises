import unittest
from kattis import k_how_many_digits

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''

        self.assertEqual(k_how_many_digits.counted( 0), 1)
        self.assertEqual(k_how_many_digits.counted( 1), 1)
        self.assertEqual(k_how_many_digits.counted( 3), 1)
        self.assertEqual(k_how_many_digits.counted(10), 7)
        self.assertEqual(k_how_many_digits.counted(20), 19)

###############################################################################

if __name__ == '__main__':
    unittest.main()
