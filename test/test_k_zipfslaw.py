import io
import unittest
from unittest.mock import patch
from kattis import k_zipfslaw

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''

        inputs = '''2

In practice, the difference between theory and practice is always
greater than the difference between theory and practice in theory.
    - Anonymous

Man will occasionally stumble over the truth, but most of the
time he will pick himself up and continue on.
    - W. S. L. Churchill
EndOfText
'''

        outputs = []
        outputs.append('between')
        outputs.append('difference')
        outputs.append('in')
        outputs.append('will')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_zipfslaw.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
