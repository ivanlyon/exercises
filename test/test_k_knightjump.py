import io
import unittest
from unittest.mock import patch
from kattis import k_knightjump

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('4')
        inputs.append('....')
        inputs.append('....')
        inputs.append('....')
        inputs.append('...K')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '2\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_knightjump.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('..K')
        inputs.append('...')
        inputs.append('###')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '-1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_knightjump.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
