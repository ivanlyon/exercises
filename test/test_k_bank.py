import io
import unittest
from unittest.mock import patch
from kattis import k_bank

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('4 4')
        inputs.append('1000 1')
        inputs.append('2000 2')
        inputs.append('500 2')
        inputs.append('1200 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '4200\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_bank.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('3 4')
        inputs.append('1000 0')
        inputs.append('2000 1')
        inputs.append('500 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '3000\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_bank.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
