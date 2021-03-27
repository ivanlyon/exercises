import io
import unittest
from unittest.mock import patch
from kattis import k_dartscores

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('5')
        inputs.append('32 -39')
        inputs.append('71 89')
        inputs.append('-60 80')
        inputs.append('0 0')
        inputs.append('196 89')
        inputs.append('5')
        inputs.append('0 0')
        inputs.append('20 0')
        inputs.append('0 20')
        inputs.append('-20 0')
        inputs.append('0 -20')
        inputs.append('1')
        inputs.append('0 -21')
        inputs.append('1')
        inputs.append('0 -200')
        inputs.append('1')
        inputs.append('0 -201')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('29')
        outputs.append('50')
        outputs.append('9')
        outputs.append('1')
        outputs.append('0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_dartscores.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
