import io
import unittest
from unittest.mock import patch
from kattis import k_statistics

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 4 10')
        inputs.append('9 2 5 6 4 5 9 2 1 4')
        inputs.append('7 6 10 1 2 5 10 9')
        inputs.append('1 9')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Case 1: 4 10 6')
        outputs.append('Case 2: 1 9 8')
        outputs.append('Case 3: 1 10 9')
        outputs.append('Case 4: 9 9 0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_statistics.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
