import io
import unittest
from unittest.mock import patch
from kattis import k_kafkaesque

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('1')
        inputs.append('23')
        inputs.append('18')
        inputs.append('13')
        inputs.append('99')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '3\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kafkaesque.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('5')
        inputs.append('11')
        inputs.append('20')
        inputs.append('33')
        inputs.append('40')
        inputs.append('55')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '1\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kafkaesque.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''
        inputs = []
        inputs.append('8')
        inputs.append('8')
        inputs.append('7')
        inputs.append('6')
        inputs.append('5')
        inputs.append('4')
        inputs.append('3')
        inputs.append('2')
        inputs.append('1')
        inputs = '\n'.join(inputs) + '\n'

        outputs = '8\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_kafkaesque.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
