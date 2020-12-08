import io
import unittest
from unittest.mock import patch
from kattis import k_unionfind

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('10 4')
        inputs.append('? 1 3')
        inputs.append('= 1 8')
        inputs.append('= 3 8')
        inputs.append('? 1 3')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('no')
        outputs.append('yes')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_unionfind.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('4 5')
        inputs.append('? 0 0')
        inputs.append('= 0 1')
        inputs.append('= 1 2')
        inputs.append('= 0 2')
        inputs.append('? 0 3')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('yes')
        outputs.append('no')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_unionfind.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
