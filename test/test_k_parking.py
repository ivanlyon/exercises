import io
import unittest
from unittest.mock import patch
from kattis import k_parking

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('5 3 1')
        inputs.append('1 6')
        inputs.append('3 5')
        inputs.append('2 8')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '33\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_parking.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('10 8 6')
        inputs.append('15 30')
        inputs.append('25 50')
        inputs.append('70 80')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '480\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_parking.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
