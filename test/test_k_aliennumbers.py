import io
import unittest
from unittest.mock import patch
from kattis import k_aliennumbers

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('4')
        inputs.append('9 0123456789 oF8')
        inputs.append('Foo oF8 0123456789')
        inputs.append('13 0123456789abcdef 01')
        inputs.append('CODE O!CDE? A?JM!.')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Case #1: Foo')
        outputs.append('Case #2: 9')
        outputs.append('Case #3: 10011')
        outputs.append('Case #4: JAM!')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_aliennumbers.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
