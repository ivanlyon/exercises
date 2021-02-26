import io
import unittest
from unittest.mock import patch
from kattis import k_armystrengtheasy

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('')
        inputs.append('1 1')
        inputs.append('1')
        inputs.append('1')
        inputs.append('')
        inputs.append('3 2')
        inputs.append('1 3 2')
        inputs.append('5 5')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Godzilla')
        outputs.append('MechaGodzilla')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_armystrengtheasy.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
