import io
import unittest
from unittest.mock import patch
from kattis import k_playfair

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('playfair example')
        inputs.append('hide the gold in the tree stump')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'BMNDZBXDKYBEJVDMUIXMMNUVIF\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_playfair.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('the magic key')
        inputs.append('i love programming competition')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'YDVHCWSPKNTAHKUBIPERMHGHDVRU\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_playfair.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
