import unittest
from kattis import k_bachetsgame

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(20, (1, 3, 8)), "Stan wins")

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(21, (1, 3, 8)), "Stan wins")

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(22, (1, 3, 8)), "Ollie wins")

    def test_sample_input_4(self):
        '''Run and assert problem statement sample 4 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(23, (1, 3, 8)), "Stan wins")

    def test_sample_input_5(self):
        '''Run and assert problem statement sample 5 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(1000000, (1, 23, 38, 11, 7, 5, 4, 8, 3, 13)), "Stan wins")

    def test_sample_input_6(self):
        '''Run and assert problem statement sample 6 input and output.'''

        self.assertEqual(k_bachetsgame.playGame(99996, (1, 23, 38, 11, 7, 5, 4, 8, 3, 13)), "Ollie wins")

###############################################################################

if __name__ == '__main__':
    unittest.main()