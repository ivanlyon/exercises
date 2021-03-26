import io
import unittest
from unittest.mock import patch
from kattis import k_babelfish

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('dog ogday')
        inputs.append('cat atcay')
        inputs.append('pig igpay')
        inputs.append('froot ootfray')
        inputs.append('loops oopslay')
        inputs.append('')
        inputs.append('atcay')
        inputs.append('ittenkay')
        inputs.append('oopslay')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('cat')
        outputs.append('eh')
        outputs.append('loops')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_babelfish.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
