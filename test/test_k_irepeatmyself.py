import io
import unittest
from unittest.mock import patch
from kattis import k_irepeatmyself

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('4')
        inputs.append('I Repeat Myself I Repeat Myself I Repeat')
        inputs.append('aaaaaaaaaaaaaaaaaaaaa')
        inputs.append('abbcabbcabbabbcabb')
        inputs.append('No repeat')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('16')
        outputs.append('1')
        outputs.append('11')
        outputs.append('9')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_irepeatmyself.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
