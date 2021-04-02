import io
import unittest
from unittest.mock import patch
from kattis import k_2048

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 0 0 2')
        inputs.append('4 16 8 2')
        inputs.append('2 64 32 4')
        inputs.append('1024 1024 64 0')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('4 0 0 0')
        outputs.append('4 16 8 2')
        outputs.append('2 64 32 4')
        outputs.append('2048 64 0 0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 0 0 2')
        inputs.append('4 16 8 2')
        inputs.append('2 64 32 4')
        inputs.append('1024 1024 64 0')
        inputs.append('1')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('2 16 8 4')
        outputs.append('4 64 32 4')
        outputs.append('2 1024 64 0')
        outputs.append('1024 0 0 0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 0 0 2')
        inputs.append('4 16 8 2')
        inputs.append('2 64 32 4')
        inputs.append('1024 1024 64 0')
        inputs.append('2')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('0 0 0 4')
        outputs.append('4 16 8 2')
        outputs.append('2 64 32 4')
        outputs.append('0 0 2048 64')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_4(self):
        '''Run and assert problem statement sample 4 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 0 0 2')
        inputs.append('4 16 8 2')
        inputs.append('2 64 32 4')
        inputs.append('1024 1024 64 0')
        inputs.append('3')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('2 0 0 0')
        outputs.append('4 16 8 0')
        outputs.append('2 64 32 4')
        outputs.append('1024 1024 64 4')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_5(self):
        '''Run and assert problem statement sample 5 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 2 4 8')
        inputs.append('4 0 4 4')
        inputs.append('16 16 16 16')
        inputs.append('32 16 16 32')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('4 4 8 0')
        outputs.append('8 4 0 0')
        outputs.append('32 32 0 0')
        outputs.append('32 32 32 0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_6(self):
        '''Run and assert problem statement sample 6 input and output.'''
        inputs, outputs = [], []
        inputs.append('2 2 4 8')
        inputs.append('4 0 4 4')
        inputs.append('16 16 16 16')
        inputs.append('32 16 16 32')
        inputs.append('2')
        inputs = '\n'.join(inputs) + '\n'

        outputs.append('0 4 4 8')
        outputs.append('0 0 4 8')
        outputs.append('0 0 32 32')
        outputs.append('0 32 32 32')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_2048.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
