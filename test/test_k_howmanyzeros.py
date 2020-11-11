import unittest
from kattis import k_howmanyzeros

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''

        self.assertEqual(k_howmanyzeros.difference(10, 11), 1)
        self.assertEqual(k_howmanyzeros.difference(100, 200), 22)
        self.assertEqual(k_howmanyzeros.difference(0, 500), 92)
        self.assertEqual(k_howmanyzeros.difference(1234567890, 2345678901), 987654304)
        self.assertEqual(k_howmanyzeros.difference(0, 4294967295), 3825876150)

###############################################################################

if __name__ == '__main__':
    unittest.main()
