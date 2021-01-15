import io
import unittest
from unittest.mock import patch
from kattis import k_dicegame

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample input 1 and output.'''
        inputs = []
        inputs.append('1 4 1 4')
        inputs.append('1 6 1 6')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'Emma\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_dicegame.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample input 2 and output.'''
        inputs = []
        inputs.append('1 8 1 8')
        inputs.append('1 10 2 5')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'Tie\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_dicegame.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample input 3 and output.'''
        inputs = []
        inputs.append('2 7 2 7')
        inputs.append('1 5 2 5')
        inputs = '\n'.join(inputs) + '\n'

        outputs = 'Gunnar\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_dicegame.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
