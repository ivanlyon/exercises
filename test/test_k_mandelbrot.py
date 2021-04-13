import io
import unittest
from unittest.mock import patch
from kattis import k_mandelbrot

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('0 0 100')
        inputs.append('1.264 -1.109 100')
        inputs.append('1.264 -1.109 10')
        inputs.append('1.264 -1.109 1')
        inputs.append('-2.914 -1.783 200')
        inputs.append('0.124 0.369 200')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Case 1: IN')
        outputs.append('Case 2: OUT')
        outputs.append('Case 3: OUT')
        outputs.append('Case 4: IN')
        outputs.append('Case 5: OUT')
        outputs.append('Case 6: IN')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_mandelbrot.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
