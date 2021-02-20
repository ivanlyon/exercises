import io
import unittest
from unittest.mock import patch
from kattis import k_nine

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('1')
        inputs.append('2')
        inputs.append('100')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('8')
        outputs.append('72')
        outputs.append('343393926')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_nine.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
