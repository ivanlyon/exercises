import io
import unittest
from unittest.mock import patch
from kattis import k_shortestpath1

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('4 3 4 0')
        inputs.append('0 1 2')
        inputs.append('1 2 2')
        inputs.append('3 0 2')
        inputs.append('0')
        inputs.append('1')
        inputs.append('2')
        inputs.append('3')
        inputs.append('2 1 1 0')
        inputs.append('0 1 100')
        inputs.append('1')
        inputs.append('0 0 0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0')
        outputs.append('2')
        outputs.append('4')
        outputs.append('Impossible')
        outputs.append('')
        outputs.append('100')
        outputs.append('')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_shortestpath1.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
