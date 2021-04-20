import io
import unittest
from unittest.mock import patch
from kattis import k_lastfactorialdigit

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('10')
        inputs.append('1')
        inputs.append('2')
        inputs.append('3')
        inputs.append('4')
        inputs.append('5')
        inputs.append('6')
        inputs.append('7')
        inputs.append('8')
        inputs.append('9')
        inputs.append('10')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1')
        outputs.append('2')
        outputs.append('6')
        outputs.append('4')
        outputs.append('0')
        outputs.append('0')
        outputs.append('0')
        outputs.append('0')
        outputs.append('0')
        outputs.append('0')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_lastfactorialdigit.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
