import io
import unittest
from unittest.mock import patch
from kattis import k_textmessaging

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('3 2 6')
        inputs.append('8 2 5 2 4 9')
        inputs.append('3 9 26')
        inputs.append('1 1 1 100 100 1 1 1 1 1 1 1 1 1 1 1 1 10 11 11 11 11 1 1 1 100')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Case #1: 47')
        outputs.append('Case #2: 397')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_textmessaging.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
