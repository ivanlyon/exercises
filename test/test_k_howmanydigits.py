import unittest
from kattis import k_howmanydigits

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''

        self.assertEqual(k_howmanydigits.counted( 0), 1)
        self.assertEqual(k_howmanydigits.counted( 1), 1)
        self.assertEqual(k_howmanydigits.counted( 3), 1)
        self.assertEqual(k_howmanydigits.counted(10), 7)
        self.assertEqual(k_howmanydigits.counted(20), 19)

###############################################################################

if __name__ == '__main__':
    unittest.main()
