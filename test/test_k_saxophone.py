import io
import unittest
from unittest.mock import patch
from kattis import k_saxophone

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('cdefgab')
        inputs.append('BAGFEDC')
        inputs.append('CbCaDCbCbCCbCbabCCbCbabae')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0 1 1 1 0 0 1 1 1 1')
        outputs.append('1 1 1 1 0 0 1 1 1 0')
        outputs.append('1 8 10 2 0 0 2 2 1 0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_saxophone.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
