import io
import unittest
from unittest.mock import patch
from kattis import k_pebblesolitaire

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('---oo-------')
        inputs.append('-o--o-oo----')
        inputs.append('-o----ooo---')
        inputs.append('oooooooooooo')
        inputs.append('oooooooooo-o')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1')
        outputs.append('2')
        outputs.append('3')
        outputs.append('12')
        outputs.append('1')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_pebblesolitaire.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
