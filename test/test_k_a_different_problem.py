import unittest
from kattis import k_a_different_problem

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertEqual(k_a_different_problem.difference(10, 12), 2)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        self.assertEqual(k_a_different_problem.difference(71293781758123, 72784), 71293781685339)

###############################################################################

if __name__ == '__main__':
    unittest.main()
