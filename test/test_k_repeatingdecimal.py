import io
import unittest
from unittest.mock import patch
from kattis import k_repeatingdecimal

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3 7 10')
        inputs.append('199 200 1')
        inputs.append('9 35 25')
        inputs.append('7 10 3')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0.4285714285')
        outputs.append('0.9')
        outputs.append('0.2571428571428571428571428')
        outputs.append('0.700')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_repeatingdecimal.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
