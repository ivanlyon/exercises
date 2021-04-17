import io
import unittest
from unittest.mock import patch
from kattis import k_quickbrownfox

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('The quick brown fox jumps over the lazy dog.')
        inputs.append('ZYXW, vu TSR Ponm lkj ihgfd CBA.')
        inputs.append('.,?!\'" 92384 abcde FGHIJ')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('pangram')
        outputs.append('missing eq')
        outputs.append('missing klmnopqrstuvwxyz')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_quickbrownfox.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
