import io
import unittest
from unittest.mock import patch
from kattis import k_permutationdescent

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('4')
        inputs.append('1 3 1')
        inputs.append('2 5 2')
        inputs.append('3 8 3')
        inputs.append('4 99 50')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1 4')
        outputs.append('2 66')
        outputs.append('3 15619')
        outputs.append('4 325091')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_permutationdescent.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
