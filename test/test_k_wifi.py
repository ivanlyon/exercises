import unittest
from kattis import k_wifi

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertGreater(k_wifi.minmax(2, (1, 3, 10)), 0.9)
        self.assertLess(k_wifi.minmax(2, (1, 3, 10)), 1.1)

###############################################################################

if __name__ == '__main__':
    unittest.main()
