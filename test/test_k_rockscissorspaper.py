import io
import unittest
from unittest.mock import patch
from kattis import k_rockscissorspaper

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('3 3 1')
        inputs.append('RRR')
        inputs.append('RSR')
        inputs.append('RRR')
        inputs.append('3 4 2')
        inputs.append('RSPR')
        inputs.append('SPRS')
        inputs.append('PRSP')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('RRR')
        outputs.append('RRR')
        outputs.append('RRR')
        outputs.append('')
        outputs.append('RRRS')
        outputs.append('RRSP')
        outputs.append('RSPR')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_rockscissorspaper.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
