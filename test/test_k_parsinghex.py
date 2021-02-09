import io
import unittest
from unittest.mock import patch
from kattis import k_parsinghex

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('uyzrr0x5206aBCtrrwm0Xa8aD4poqwqr')
        inputs.append('pqovx0x6d3e6-+ 230xB6fcgmmm')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0x5206aBC 86010556')
        outputs.append('0Xa8aD4 690900')
        outputs.append('0x6d3e6 447462')
        outputs.append('0xB6fc 46844')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_parsinghex.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
