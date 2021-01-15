import io
import unittest
from unittest.mock import patch
from kattis import k_sumkindofproblem

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('1 1')
        inputs.append('2 10')
        inputs.append('3 1001')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1 1 1 2')
        outputs.append('2 55 100 110')
        outputs.append('3 501501 1002001 1003002')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sumkindofproblem.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
