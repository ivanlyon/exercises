import io
import unittest
from unittest.mock import patch
from kattis import k_matchsticks

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('3')
        inputs.append('6')
        inputs.append('7')
        inputs.append('15')
        inputs.append('10')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('7 7')
        outputs.append('6 111')
        outputs.append('8 711')
        outputs.append('108 7111111')
        outputs.append('22 11111')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_matchsticks.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
