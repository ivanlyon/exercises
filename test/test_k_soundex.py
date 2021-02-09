import io
import unittest
from unittest.mock import patch
from kattis import k_soundex

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('KHAWN')
        inputs.append('PFISTER')
        inputs.append('BOBBY')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('25')
        outputs.append('1236')
        outputs.append('11')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_soundex.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
