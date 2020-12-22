import io
import unittest
from unittest.mock import patch
from kattis import k_intervalcover

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('-0.5 1')
        inputs.append('3')
        inputs.append('-0.9 -0.1')
        inputs.append('-0.2 2')
        inputs.append('-0.7 1')
        inputs.append('0 1')
        inputs.append('3')
        inputs.append('0 0.25')
        inputs.append('0.25 0.75')
        inputs.append('0.75 0.999')
        inputs.append('0 1')
        inputs.append('3')
        inputs.append('0 0.25')
        inputs.append('0.25 0.75')
        inputs.append('0.75 1')
        inputs.append('1 1')
        inputs.append('1')
        inputs.append('1 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1')
        outputs.append('2')
        outputs.append('impossible')
        outputs.append('3')
        outputs.append('0 1 2')
        outputs.append('1')
        outputs.append('0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_intervalcover.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
