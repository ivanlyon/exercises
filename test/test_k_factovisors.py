import io
import unittest
from unittest.mock import patch
from kattis import k_factovisors

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('6 9')
        inputs.append('6 27')
        inputs.append('20 10000')
        inputs.append('20 100000')
        inputs.append('1000 1009')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('9 divides 6!')
        outputs.append('27 does not divide 6!')
        outputs.append('10000 divides 20!')
        outputs.append('100000 does not divide 20!')
        outputs.append('1009 does not divide 1000!')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_factovisors.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
