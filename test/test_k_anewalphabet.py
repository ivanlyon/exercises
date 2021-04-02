import io
import unittest
from unittest.mock import patch
from kattis import k_anewalphabet

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = 'All your base are belong to us.\n'
        outputs = "@11 `/0|_||Z 8@$3 @|Z3 8310[]\[]6 ']['0 |_|$.\n"

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_anewalphabet.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = "What's the Frequency, Kenneth?\n"
        outputs = "\/\/[-]@'][''$ ']['[-]3 #|Z3(,)|_|3[]\[](`/, |<3[]\[][]\[]3']['[-]?\n"

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_anewalphabet.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = 'A new alphabet!\n'
        outputs = "@ []\[]3\/\/ @1|D[-]@83']['!\n"

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_anewalphabet.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
