import io
import unittest
from unittest.mock import patch
from kattis import k_longincsubseq

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('10')
        inputs.append('1 2 3 4 5 6 7 8 9 10')
        inputs.append('10')
        inputs.append('1 1 1 1 1 1 1 1 1 1')
        inputs.append('10')
        inputs.append('5 19 5 81 50 28 29 1 83 23')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('10')
        outputs.append('0 1 2 3 4 5 6 7 8 9')
        outputs.append('1')
        outputs.append('0')
        outputs.append('5')
        outputs.append('0 1 5 6 8')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_longincsubseq.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_others(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('10')
        inputs.append('10 9 8 7 6 5 4 3 2 1')
        inputs.append('10')
        inputs.append('23 83 1 29 28 29 50 81 19 5')
        inputs.append('1')
        inputs.append('999')
        inputs.append('10')
        inputs.append('-1 -2 -3 -4 -5 -6 -7 -8 -9 -10')
        inputs.append('10')
        inputs.append('-1 -1 -1 -1 -1 -1 -1 -1 -1 -1')
        inputs.append('10')
        inputs.append('-5 -19 -5 -81 -50 -28 -29 -1 -83 -23')
        inputs.append('10')
        inputs.append('-10 -9 -8 -7 -6 -5 -4 -3 -2 -1')
        inputs.append('10')
        inputs.append('11 12 13 14 5 6 7 8 9 10')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1')
        outputs.append('0')
        outputs.append('5')
        outputs.append('2 4 5 6 7')
        outputs.append('1')
        outputs.append('0')
        outputs.append('1')
        outputs.append('0')
        outputs.append('1')
        outputs.append('0')
        outputs.append('4')
        outputs.append('3 4 6 7')
        outputs.append('10')
        outputs.append('0 1 2 3 4 5 6 7 8 9')
        outputs.append('6')
        outputs.append('4 5 6 7 8 9')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_longincsubseq.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
