import io
import unittest
from unittest.mock import patch
from kattis import k_persistent

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('0')
        inputs.append('1')
        inputs.append('4')
        inputs.append('7')
        inputs.append('18')
        inputs.append('49')
        inputs.append('51')
        inputs.append('768')
        inputs.append('-1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('10')
        outputs.append('11')
        outputs.append('14')
        outputs.append('17')
        outputs.append('29')
        outputs.append('77')
        outputs.append('There is no such number.')
        outputs.append('2688')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_persistent.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
