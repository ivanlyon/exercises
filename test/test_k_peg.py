import io
import unittest
from unittest.mock import patch
from kattis import k_peg

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('  ooo  ')
        inputs.append('  ooo  ')
        inputs.append('ooooooo')
        inputs.append('ooo.ooo')
        inputs.append('ooooooo')
        inputs.append('  ooo  ')
        inputs.append('  ooo  ')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '4\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_peg.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('  ooo  ')
        inputs.append('  ooo  ')
        inputs.append('..ooo..')
        inputs.append('oo...oo')
        inputs.append('..ooo..')
        inputs.append('  ooo  ')
        inputs.append('  ooo  ')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '12\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_peg.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
