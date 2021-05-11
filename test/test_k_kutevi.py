import io
import unittest
from unittest.mock import patch
from kattis import k_kutevi

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('2 1')
        inputs.append('30 70')
        inputs.append('40')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'YES\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kutevi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('1 1')
        inputs.append('100')
        inputs.append('60')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'YES\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kutevi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = []
        inputs.append('3 2')
        inputs.append('10 20 30')
        inputs.append('5 70')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'NO\nYES\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kutevi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
