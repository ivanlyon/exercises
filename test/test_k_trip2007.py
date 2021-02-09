import io
import unittest
from unittest.mock import patch
from kattis import k_trip2007

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('6')
        inputs.append('1 1 2 2 2 3')
        inputs.append('6')
        inputs.append('1 1 2 2 2 3')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('3')
        outputs.append('2 1')
        outputs.append('2 1')
        outputs.append('2 3')
        outputs.append('')
        outputs.append('3')
        outputs.append('2 1')
        outputs.append('2 1')
        outputs.append('2 3')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_trip2007.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
