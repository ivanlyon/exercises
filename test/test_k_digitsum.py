import io
import unittest
from unittest.mock import patch
from kattis import k_digitsum

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('0 10')
        inputs.append('28 31')
        inputs.append('1234 56789')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('46')
        outputs.append('28')
        outputs.append('1128600')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_digitsum.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
