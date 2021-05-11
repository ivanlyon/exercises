import io
import unittest
from unittest.mock import patch
from kattis import k_joinstrings

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('4')
        inputs.append('cute')
        inputs.append('cat')
        inputs.append('kattis')
        inputs.append('is')
        inputs.append('3 2')
        inputs.append('4 1')
        inputs.append('3 4')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'kattiscatiscute\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_joinstrings.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('howis')
        inputs.append('this')
        inputs.append('practicalexam')
        inputs.append('1 2')
        inputs.append('1 3')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'howisthispracticalexam\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_joinstrings.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
