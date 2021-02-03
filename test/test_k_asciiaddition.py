import io
import unittest
from unittest.mock import patch
from kattis import k_asciiaddition

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx')
        inputs.append('....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x')
        inputs.append('....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x')
        inputs.append('....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x')
        inputs.append('....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x')
        inputs.append('....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x')
        inputs.append('....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('....x.xxxxx.xxxxx.xxxxx.x...x.xxxxx.xxxxx')
        outputs.append('....x.....x.....x.x.....x...x.x.........x')
        outputs.append('....x.....x.....x.x.....x...x.x.........x')
        outputs.append('....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x')
        outputs.append('....x.x.........x.....x.....x.....x.....x')
        outputs.append('....x.x.........x.....x.....x.....x.....x')
        outputs.append('....x.xxxxx.xxxxx.xxxxx.....x.xxxxx.....x')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_asciiaddition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_all_digits(self):
        '''Run and assert problem statement printing all digits.'''
        inputs = []
        inputs.append('....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.......xxxxx')
        inputs.append('....x.....x.....x.x...x.x.....x.........x.x...x.x...x.x...x...x...x...x')
        inputs.append('....x.....x.....x.x...x.x.....x.........x.x...x.x...x.x...x...x...x...x')
        inputs.append('....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.x...x.xxxxx.x...x')
        inputs.append('....x.x.........x.....x.....x.x...x.....x.x...x.....x.x...x...x...x...x')
        inputs.append('....x.x.........x.....x.....x.x...x.....x.x...x.....x.x...x...x...x...x')
        inputs.append('....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.......xxxxx')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx')
        outputs.append('....x.....x.....x.x...x.x.....x.........x.x...x.x...x.x...x')
        outputs.append('....x.....x.....x.x...x.x.....x.........x.x...x.x...x.x...x')
        outputs.append('....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.x...x')
        outputs.append('....x.x.........x.....x.....x.x...x.....x.x...x.....x.x...x')
        outputs.append('....x.x.........x.....x.....x.x...x.....x.x...x.....x.x...x')
        outputs.append('....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_asciiaddition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_zeroes(self):
        '''Run and assert problem statement printing all digits.'''
        inputs = []
        inputs.append('xxxxx.......xxxxx')
        inputs.append('x...x...x...x...x')
        inputs.append('x...x...x...x...x')
        inputs.append('x...x.xxxxx.x...x')
        inputs.append('x...x...x...x...x')
        inputs.append('x...x...x...x...x')
        inputs.append('xxxxx.......xxxxx')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('xxxxx')
        outputs.append('x...x')
        outputs.append('x...x')
        outputs.append('x...x')
        outputs.append('x...x')
        outputs.append('x...x')
        outputs.append('xxxxx')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_asciiaddition.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
