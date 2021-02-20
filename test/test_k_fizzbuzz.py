import io
import unittest
from unittest.mock import patch
from kattis import k_fizzbuzz

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = '2 3 7\n'

        outputs = []
        outputs.append('1')
        outputs.append('Fizz')
        outputs.append('Buzz')
        outputs.append('Fizz')
        outputs.append('5')
        outputs.append('FizzBuzz')
        outputs.append('7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_fizzbuzz.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = '2 4 7\n'

        outputs = []
        outputs.append('1')
        outputs.append('Fizz')
        outputs.append('3')
        outputs.append('FizzBuzz')
        outputs.append('5')
        outputs.append('Fizz')
        outputs.append('7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_fizzbuzz.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = '3 5 7\n'

        outputs = []
        outputs.append('1')
        outputs.append('2')
        outputs.append('Fizz')
        outputs.append('4')
        outputs.append('Buzz')
        outputs.append('Fizz')
        outputs.append('7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_fizzbuzz.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
