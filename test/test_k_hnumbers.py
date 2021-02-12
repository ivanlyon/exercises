import io
import unittest
from unittest.mock import patch
from kattis import k_hnumbers

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('21')
        inputs.append('85')
        inputs.append('789')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('21 0')
        outputs.append('85 5')
        outputs.append('789 62')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_hnumbers.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
