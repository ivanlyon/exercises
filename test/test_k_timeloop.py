import unittest
from kattis import k_timeloop

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        result = []
        result.append('1 Abradabra')
        result.append('2 Abradabra')
        result.append('3 Abradabra')
        result.append('4 Abradabra')
        result.append('5 Abradabra')
        self.assertEqual(k_timeloop.createOutput(5), result)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        result = []
        result.append('1 Abradabra')
        result.append('2 Abradabra')
        result.append('3 Abradabra')
        result.append('4 Abradabra')
        result.append('5 Abradabra')
        result.append('6 Abradabra')
        result.append('7 Abradabra')
        result.append('8 Abradabra')
        result.append('9 Abradabra')
        result.append('10 Abradabra')
        self.assertEqual(k_timeloop.createOutput(10), result)

###############################################################################

if __name__ == '__main__':
    unittest.main()
