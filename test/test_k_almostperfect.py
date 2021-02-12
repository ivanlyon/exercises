import io
import unittest
from unittest.mock import patch
from kattis import k_almostperfect

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('6')
        inputs.append('65')
        inputs.append('650')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('6 perfect')
        outputs.append('65 not perfect')
        outputs.append('650 almost perfect')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_almostperfect.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
