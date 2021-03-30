import io
import unittest
from unittest.mock import patch
from kattis import k_multiplicationgame

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('10')
        inputs.append('10 Alice')
        inputs.append('20 Bob')
        inputs.append('30 Alice')
        inputs.append('40 Bob')
        inputs.append('50 Alice')
        inputs.append('60 Bob')
        inputs.append('70 Alice')
        inputs.append('80 Bob')
        inputs.append('90 Alice')
        inputs.append('100 Bob')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Bob')
        outputs.append('Bob')
        outputs.append('tie')
        outputs.append('tie')
        outputs.append('Alice')
        outputs.append('tie')
        outputs.append('tie')
        outputs.append('tie')
        outputs.append('tie')
        outputs.append('Alice')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_multiplicationgame.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
