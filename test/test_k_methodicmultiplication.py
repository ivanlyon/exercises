import io
import unittest
from unittest.mock import patch
from kattis import k_methodicmultiplication

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample input 1 and output.'''
        inputs = []
        inputs.append('S(S(0))')
        inputs.append('S(S(S(0)))')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'S(S(S(S(S(S(0))))))\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_methodicmultiplication.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample input 2 and output.'''
        inputs = []
        inputs.append('S(S(S(S(S(0)))))')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '0\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_methodicmultiplication.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
