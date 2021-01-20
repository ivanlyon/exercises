import io
import unittest
from unittest.mock import patch
from kattis import k_digits

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('42')
        inputs.append('5')
        inputs.append('END')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('3')
        outputs.append('2')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_digits.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_search_for_wa(self):
        '''Run and assert attempts to reproduce WA.'''
        inputs = []
        inputs.append('42 ')
        inputs.append('5')
        inputs.append('1')
        inputs.append('0')
        inputs.append('10')
        inputs.append('12345678901')
        inputs.append('END')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('3')
        outputs.append('2')
        outputs.append('1')
        outputs.append('2')
        outputs.append('3')
        outputs.append('4')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_digits.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
