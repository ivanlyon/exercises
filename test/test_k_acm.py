import io
import unittest
from unittest.mock import patch
from kattis import k_acm

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('3 E right')
        inputs.append('10 A wrong')
        inputs.append('30 C wrong')
        inputs.append('50 B wrong')
        inputs.append('100 A wrong')
        inputs.append('200 A right')
        inputs.append('250 C wrong')
        inputs.append('300 D right')
        inputs.append('-1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '3 543\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_acm.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('7 H right')
        inputs.append('15 B wrong')
        inputs.append('30 E wrong')
        inputs.append('35 E right')
        inputs.append('80 B wrong')
        inputs.append('80 B right')
        inputs.append('100 D wrong')
        inputs.append('100 C wrong')
        inputs.append('300 C right')
        inputs.append('300 D wrong')
        inputs.append('-1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '4 502\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_acm.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
