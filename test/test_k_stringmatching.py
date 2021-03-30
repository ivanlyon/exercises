import io
import unittest
from unittest.mock import patch
from kattis import k_stringmatching

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('p')
        inputs.append('Popup')
        inputs.append('helo')
        inputs.append('Hello there!')
        inputs.append('peek a boo')
        inputs.append('you speek a bootiful language')
        inputs.append('anas')
        inputs.append('bananananaspaj')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('2 4')
        outputs.append('')
        outputs.append('5')
        outputs.append('7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_stringmatching.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
