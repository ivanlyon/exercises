import io
import unittest
from unittest.mock import patch
from kattis import k_autori

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = 'Knuth-Morris-Pratt\n'
        outputs = 'KMP\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_autori.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = 'Mirko-Slavko\n'
        outputs = 'MS\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_autori.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
