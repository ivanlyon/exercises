import unittest
from kattis import k_ladder

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertEqual(k_ladder.compute_length(500, 70), 533)

###############################################################################

if __name__ == '__main__':
    unittest.main()
