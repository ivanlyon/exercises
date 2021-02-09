import io
import unittest
from unittest.mock import patch
from kattis import k_loowater

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 3')
        inputs.append('5')
        inputs.append('4')
        inputs.append('7')
        inputs.append('8')
        inputs.append('4')
        inputs.append('2 1')
        inputs.append('5')
        inputs.append('5')
        inputs.append('10')
        inputs.append('0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('11')
        outputs.append('Loowater is doomed!')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_loowater.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
