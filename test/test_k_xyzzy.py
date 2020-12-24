import io
import unittest
from unittest.mock import patch
from kattis import k_xyzzy

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('0 1 2')
        inputs.append('-60 1 3')
        inputs.append('-60 1 4')
        inputs.append('20 1 5')
        inputs.append('0 0')
        inputs.append('5')
        inputs.append('0 1 2')
        inputs.append('20 1 3')
        inputs.append('-60 1 4')
        inputs.append('-60 1 5')
        inputs.append('0 0')
        inputs.append('5')
        inputs.append('0 1 2')
        inputs.append('21 1 3')
        inputs.append('-60 1 4')
        inputs.append('-60 1 5')
        inputs.append('0 0')
        inputs.append('5')
        inputs.append('0 1 2')
        inputs.append('20 2 1 3')
        inputs.append('-60 1 4')
        inputs.append('-60 1 5')
        inputs.append('0 0')
        inputs.append('-1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('hopeless')
        outputs.append('hopeless')
        outputs.append('winnable')
        outputs.append('winnable')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_xyzzy.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_no_path(self):
        '''No path from 1 to last node.'''
        inputs = []
        inputs.append('5')
        inputs.append('0 1 2')
        inputs.append('60 1 3')
        inputs.append('60 1 4')
        inputs.append('20 1') # line break for test
        inputs.append('2')
        inputs.append('0 0')
        inputs.append('-1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('hopeless')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_xyzzy.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
