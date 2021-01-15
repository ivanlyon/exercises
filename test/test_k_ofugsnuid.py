import io
import unittest
from unittest.mock import patch
from kattis import k_ofugsnuid

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample input 1 and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('1')
        inputs.append('2')
        inputs.append('3')
        inputs.append('4')
        inputs.append('5')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('5')
        outputs.append('4')
        outputs.append('3')
        outputs.append('2')
        outputs.append('1')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_ofugsnuid.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample input 2 and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('10')
        inputs.append('12')
        inputs.append('9')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('9')
        outputs.append('12')
        outputs.append('10')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_ofugsnuid.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
