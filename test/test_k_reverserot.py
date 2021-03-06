import io
import unittest
from unittest.mock import patch
from kattis import k_reverserot

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('1 ABCD')
        inputs.append('3 YO_THERE.')
        inputs.append('1 .DOT')
        inputs.append('14 ROAD')
        inputs.append('9 SHIFTING_AND_ROTATING_IS_NOT_ENCRYPTING')
        inputs.append('2 STRING_TO_BE_CONVERTED')
        inputs.append('1 SNQZDRQDUDQ')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('EDCB')
        outputs.append('CHUHKWBR.')
        outputs.append('UPEA')
        outputs.append('ROAD')
        outputs.append('PWRAYF_LWNHAXWH.RHPWRAJAX_HMWJHPWRAORQ.')
        outputs.append('FGVTGXPQEAGDAQVAIPKTVU')
        outputs.append('REVERSE_ROT')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_reverserot.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
