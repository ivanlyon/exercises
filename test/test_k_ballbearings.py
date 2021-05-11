import io
import unittest
from unittest.mock import patch
from kattis import k_ballbearings

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('20 1 0.1')
        inputs.append('100.0 13.0 0.2')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('54')
        outputs.append('20')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_ballbearings.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
