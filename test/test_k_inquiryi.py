import io
import unittest
from unittest.mock import patch
from kattis import k_inquiryi

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('2')
        inputs.append('1')
        inputs.append('4')
        inputs.append('3')
        inputs.append('5')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '168\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_inquiryi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('1')
        inputs.append('1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_inquiryi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = []
        inputs.append('10')
        inputs.append('8')
        inputs.append('5')
        inputs.append('10')
        inputs.append('9')
        inputs.append('1')
        inputs.append('4')
        inputs.append('12')
        inputs.append('6')
        inputs.append('3')
        inputs.append('13')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '10530\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_inquiryi.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
