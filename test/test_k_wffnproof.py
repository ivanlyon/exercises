import io
import unittest
from unittest.mock import patch
from kattis import k_wffnproof

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('qKpNq')
        inputs.append('KKN')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('KqNq')
        outputs.append('no WFF possible')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_wffnproof.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
