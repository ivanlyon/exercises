import unittest
from kattis import k_everywhere

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        input1 = []
        input1.append('saskatoon')
        input1.append('toronto')
        input1.append('winnipeg')
        input1.append('toronto')
        input1.append('vancouver')
        input1.append('saskatoon')
        input1.append('toronto')
        self.assertEqual(k_everywhere.uniques(input1), 4)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        input2 = []
        input2.append('edmonton')
        input2.append('edmonton')
        input2.append('edmonton')
        self.assertEqual(k_everywhere.uniques(input2), 1)

###############################################################################

if __name__ == '__main__':
    unittest.main()
