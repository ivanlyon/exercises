import io
import unittest
from unittest.mock import patch
from kattis import k_4thought

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('9')
        inputs.append('0')
        inputs.append('7')
        inputs.append('11')
        inputs.append('24')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('4 / 4 + 4 + 4 = 9')
        outputs.append('4 / 4 / 4 / 4 = 0')
        outputs.append('4 - 4 / 4 + 4 = 7')
        outputs.append('no solution')
        outputs.append('4 * 4 + 4 + 4 = 24')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_4thought.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
