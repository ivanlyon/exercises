import io
import unittest
from unittest.mock import patch
from kattis import k_smallestmultiple

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 3 5')
        inputs.append('1 2 3 4')
        inputs.append('399 772 163 959 242')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('30')
        outputs.append('12')
        outputs.append('832307365428')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_smallestmultiple.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
