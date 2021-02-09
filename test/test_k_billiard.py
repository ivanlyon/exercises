import io
import unittest
from unittest.mock import patch
from kattis import k_billiard

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('100 100 1 1 1')
        inputs.append('200 100 5 3 4')
        inputs.append('201 132 48 1900 156')
        inputs.append('0 0 0 0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('45.00 141.42')
        outputs.append('33.69 144.22')
        outputs.append('3.09 7967.81')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_billiard.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
