import io
import unittest
from unittest.mock import patch
from kattis import k_quantumsuperposition

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('3 2 3 1')
        inputs.append('1 2')
        inputs.append('1 3')
        inputs.append('2 3')
        inputs.append('1 2')
        inputs.append('5')
        inputs.append('0')
        inputs.append('1')
        inputs.append('2')
        inputs.append('3')
        inputs.append('4')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('No')
        outputs.append('No')
        outputs.append('Yes')
        outputs.append('Yes')
        outputs.append('No')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_quantumsuperposition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_zero_edges(self):
        '''Run and assert test case with zero edges in graph'''
        inputs = []
        inputs.append('1 1 0 0')
        inputs.append('2')
        inputs.append('0')
        inputs.append('1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Yes')
        outputs.append('No')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_quantumsuperposition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_one_edge(self):
        '''Run and assert test case with one edge in 1st graph and zero in 2nd'''
        inputs = []
        inputs.append('3 1 1 0')
        inputs.append('1 3')
        inputs.append('3')
        inputs.append('0')
        inputs.append('1')
        inputs.append('2')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('No')
        outputs.append('Yes')
        outputs.append('No')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_quantumsuperposition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_all_yes(self):
        '''Run and assert test case with all results being Yes'''
        inputs = []
        inputs.append('3 2 3 1')
        inputs.append('1 2')
        inputs.append('1 3')
        inputs.append('2 3')
        inputs.append('1 2')
        inputs.append('2')
        inputs.append('2')
        inputs.append('3')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Yes')
        outputs.append('Yes')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_quantumsuperposition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
