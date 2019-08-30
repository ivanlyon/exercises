import unittest
from problems import k_vauvau

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        dogs = [2, 2, 3, 3]

        self.assertEqual(k_vauvau.how_many_attack(dogs, 1), 'both')
        self.assertEqual(k_vauvau.how_many_attack(dogs, 3), 'one')
        self.assertEqual(k_vauvau.how_many_attack(dogs, 4), 'none')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        dogs = [2, 3, 4, 5]

        self.assertEqual(k_vauvau.how_many_attack(dogs, 4), 'one')
        self.assertEqual(k_vauvau.how_many_attack(dogs, 9), 'none')
        self.assertEqual(k_vauvau.how_many_attack(dogs, 5), 'none')

###############################################################################

if __name__ == '__main__':
    unittest.main()
