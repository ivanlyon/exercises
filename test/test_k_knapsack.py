import io
import unittest
from unittest.mock import patch
from kattis import k_knapsack

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5 3')
        inputs.append('1 5')
        inputs.append('10 5')
        inputs.append('100 5')
        inputs.append('6 4')
        inputs.append('5 4')
        inputs.append('4 3')
        inputs.append('3 2')
        inputs.append('2 1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1')
        outputs.append('2')
        outputs.append('3')
        outputs.append('1 2 3')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_knapsack.main(inorder=True)
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_all_too_heavy(self):
        '''Run and assert input producing no packed result.'''
        inputs = []
        inputs.append('5 3')
        inputs.append('1 6')
        inputs.append('10 6')
        inputs.append('100 6')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0')
        outputs.append('')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_knapsack.main(inorder=True)
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_non_greedy(self):
        '''Attempt to test input that fails greedy algorithm.'''
        inputs = []
        inputs.append('10 4')
        inputs.append('1000 6')
        inputs.append('100 3')
        inputs.append('51 2')
        inputs.append('51 2')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('3')
        outputs.append('0 2 3')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_knapsack.main(inorder=True)
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
