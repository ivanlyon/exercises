import io
import unittest
from unittest.mock import patch
from kattis import k_modulosolitaire

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5 2 1')
        inputs.append('2 1')
        inputs.append('3 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '2\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_modulosolitaire.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_other_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('6 1 1')
        inputs.append('2 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '-1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_modulosolitaire.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
