import io
import unittest
from unittest.mock import patch
from kattis import k_gamerank

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_inputs(self):
        '''Run and assert problem statement sample inputs and outputs.'''
        inputs = []
        inputs.append('WW')
        inputs.append('WWW')
        inputs.append('WWWW')
        inputs.append('WLWLWLWL')
        inputs.append('WWWWWWWWWLLWW')
        inputs.append('WWWWWWWWWLWWL')

        outputs = []
        outputs.append('25')
        outputs.append('24')
        outputs.append('23')
        outputs.append('24')
        outputs.append('19')
        outputs.append('18')

        for i, j in zip(inputs, outputs):
            with patch('sys.stdin', io.StringIO(i)) as stdin,\
                 patch('sys.stdout', new_callable=io.StringIO) as stdout:
                k_gamerank.main()
                self.assertEqual(stdout.getvalue(), j + '\n')
                self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
