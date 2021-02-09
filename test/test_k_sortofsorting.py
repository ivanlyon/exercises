import io
import unittest
from unittest.mock import patch
from kattis import k_sortofsorting

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('Mozart')
        inputs.append('Beethoven')
        inputs.append('Bach')
        inputs.append('5')
        inputs.append('Hilbert')
        inputs.append('Godel')
        inputs.append('Poincare')
        inputs.append('Ramanujan')
        inputs.append('Pochhammer')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Bach')
        outputs.append('Beethoven')
        outputs.append('Mozart')
        outputs.append('')
        outputs.append('Godel')
        outputs.append('Hilbert')
        outputs.append('Poincare')
        outputs.append('Pochhammer')
        outputs.append('Ramanujan')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sortofsorting.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
