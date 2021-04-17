import io
import unittest
from unittest.mock import patch
from kattis import k_ones

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('7')
        inputs.append('9901')
        inputs.append('1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('3')
        outputs.append('6')
        outputs.append('12')
        outputs.append('1')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_ones.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
