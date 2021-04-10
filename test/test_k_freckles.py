import io
import unittest
from unittest.mock import patch
from kattis import k_freckles

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('1')
        inputs.append('')
        inputs.append('3')
        inputs.append('1.0 1.0')
        inputs.append('2.0 2.0')
        inputs.append('2.0 4.0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '3.41\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_freckles.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
