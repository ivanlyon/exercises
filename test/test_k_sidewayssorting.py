import io
import unittest
from unittest.mock import patch
from kattis import k_sidewayssorting

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3 3')
        inputs.append('oTs')
        inputs.append('nwi')
        inputs.append('eox')
        inputs.append('3 4')
        inputs.append('xAxa')
        inputs.append('yByb')
        inputs.append('zCyc')
        inputs.append('0 0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('osT')
        outputs.append('niw')
        outputs.append('exo')
        outputs.append('')
        outputs.append('Aaxx')
        outputs.append('Bbyy')
        outputs.append('Ccyz')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_sidewayssorting.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
