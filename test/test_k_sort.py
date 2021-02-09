import io
import unittest
from unittest.mock import patch
from kattis import k_sort

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('5 2')
        inputs.append('2 1 2 1 2')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '2 2 2 1 1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sort.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('9 3')
        inputs.append('1 3 3 3 2 2 2 1 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1 1 1 3 3 3 2 2 2\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sort.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = []
        inputs.append('9 77')
        inputs.append('11 33 11 77 54 11 25 25 33')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '11 11 11 33 33 25 25 77 54\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sort.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
