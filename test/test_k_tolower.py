import io
import unittest
from unittest.mock import patch
from kattis import k_tolower

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 2')
        inputs.append('abc')
        inputs.append('Def')
        inputs.append('DDG')
        inputs.append('add')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_tolower.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
