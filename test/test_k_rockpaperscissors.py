import io
import unittest
from unittest.mock import patch
from kattis import k_rockpaperscissors

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 4')
        inputs.append('1 rock 2 paper')
        inputs.append('1 scissors 2 paper')
        inputs.append('1 rock 2 rock')
        inputs.append('2 rock 1 scissors')
        inputs.append('2 1')
        inputs.append('1 rock 2 paper')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0.333')
        outputs.append('0.667')
        outputs.append('')
        outputs.append('0.000')
        outputs.append('1.000')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_rockpaperscissors.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
