import io
import unittest
from unittest.mock import patch
from kattis import k_amultiplicationgame

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('162')
        inputs.append('17')
        inputs.append('34012226')
        inputs.append('4294967295')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Stan wins.')
        outputs.append('Ollie wins.')
        outputs.append('Stan wins.')
        outputs.append('Stan wins.')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_amultiplicationgame.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
