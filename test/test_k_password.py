import io
import unittest
from unittest.mock import patch
from kattis import k_password

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('123456 0.6666')
        inputs.append('qwerty 0.3334')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1.3334\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_password.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('qwerty 0.5432')
        inputs.append('123456 0.3334')
        inputs.append('password 0.1234')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1.5802\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_password.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
