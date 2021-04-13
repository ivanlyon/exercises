import io
import unittest
from unittest.mock import patch
from kattis import k_cantor

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('0')
        inputs.append('1')
        inputs.append('0.875')
        inputs.append('END')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('MEMBER')
        outputs.append('MEMBER')
        outputs.append('NON-MEMBER')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_cantor.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
