import io
import unittest
from unittest.mock import patch
from kattis import k_delimitersoup

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = '8\n([] [] ]\n'
        outputs = '] 7\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_delimitersoup.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = '13\n(([] [[]] ())\n'
        outputs = 'ok so far\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_delimitersoup.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = '21\n[ { { () () () () } ]\n'
        outputs = '] 20\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_delimitersoup.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_4(self):
        '''Run and assert problem statement sample 4 input and output.'''
        inputs = '27\n[ { [[()]] (({})) } ] () {}\n'
        outputs = 'ok so far\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_delimitersoup.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_missing_lhs(self):
        '''Run and assert input of rhs delimiter only.'''
        inputs = '1\n}\n'
        outputs = '} 0\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_delimitersoup.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
