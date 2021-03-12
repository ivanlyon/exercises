import io
import unittest
from unittest.mock import patch
from kattis import k_modulararithmetic

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('1000 3')
        inputs.append('1 / 999')
        inputs.append('1 / 998')
        inputs.append('578 * 178')
        inputs.append('13 4')
        inputs.append('7 / 9')
        inputs.append('9 * 3')
        inputs.append('0 - 9')
        inputs.append('10 + 10')
        inputs.append('0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('999')
        outputs.append('-1')
        outputs.append('884')
        outputs.append('8')
        outputs.append('1')
        outputs.append('4')
        outputs.append('7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_modulararithmetic.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
