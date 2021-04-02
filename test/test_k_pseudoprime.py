import io
import unittest
from unittest.mock import patch
from kattis import k_pseudoprime

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3 2')
        inputs.append('10 3')
        inputs.append('341 2')
        inputs.append('341 3')
        inputs.append('1105 2')
        inputs.append('1105 3')
        inputs.append('0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('no')
        outputs.append('no')
        outputs.append('yes')
        outputs.append('no')
        outputs.append('yes')
        outputs.append('yes')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_pseudoprime.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
