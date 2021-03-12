import io
import unittest
from unittest.mock import patch
from kattis import k_backspace

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample inputs and outputs.'''
        inputs = []
        inputs.append('a<bc<')
        inputs.append('foss<<rritun')
        inputs.append('a<a<a<aa<<')

        outputs = []
        outputs.append('b')
        outputs.append('forritun')
        outputs.append('')

        for i, j in zip(inputs, outputs):
            with patch('sys.stdin', io.StringIO(i)) as stdin,\
                 patch('sys.stdout', new_callable=io.StringIO) as stdout:
                k_backspace.main()
                self.assertEqual(stdout.getvalue(), j + '\n')
                self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
