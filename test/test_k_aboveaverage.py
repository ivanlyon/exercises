import io
import unittest
from unittest.mock import patch
from kattis import k_aboveaverage

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('6')
        inputs.append('5 50 50 70 80 100')
        inputs.append('7 100 95 90 80 70 60 50')
        inputs.append('3 70 90 80')
        inputs.append('3 70 90 81')
        inputs.append('9 100 99 98 97 96 95 94 93 91')
        inputs.append('1 70')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('40.000%')
        outputs.append('57.143%')
        outputs.append('33.333%')
        outputs.append('66.667%')
        outputs.append('55.556%')
        outputs.append('0.000%')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_aboveaverage.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
