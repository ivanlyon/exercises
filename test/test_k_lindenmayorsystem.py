import io
import unittest
from unittest.mock import patch
from kattis import k_lindenmayorsystem

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2 4')
        inputs.append('A -> AB')
        inputs.append('B -> A')
        inputs.append('A')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'ABAABABA\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_lindenmayorsystem.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_zero_moves(self):
        '''Run and assert input remains unchanged after zero iterations.'''
        inputs = []
        inputs.append('2 0')
        inputs.append('A -> AB')
        inputs.append('B -> A')
        inputs.append('A')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'A\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_lindenmayorsystem.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_constant_letter(self):
        '''Run and assert test case with unchanging letters of input.'''
        inputs = []
        inputs.append('2 4')
        inputs.append('A -> AB')
        inputs.append('B -> A')
        inputs.append('ZAP')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'ZABAABABAP\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_lindenmayorsystem.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
