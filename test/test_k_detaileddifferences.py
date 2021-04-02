import io
import unittest
from unittest.mock import patch
from kattis import k_detaileddifferences

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('ATCCGCTTAGAGGGATT')
        inputs.append('GTCCGTTTAGAAGGTTT')
        inputs.append('abcdefghijklmnopqrstuvwxyz')
        inputs.append('bcdefghijklmnopqrstuvwxyza')
        inputs.append('abcdefghijklmnopqrstuvwxyz0123456789')
        inputs.append('abcdefghijklmnopqrstuvwxyz0123456789')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('ATCCGCTTAGAGGGATT')
        outputs.append('GTCCGTTTAGAAGGTTT')
        outputs.append('*....*.....*..*..')
        outputs.append('')
        outputs.append('abcdefghijklmnopqrstuvwxyz')
        outputs.append('bcdefghijklmnopqrstuvwxyza')
        outputs.append('**************************')
        outputs.append('')
        outputs.append('abcdefghijklmnopqrstuvwxyz0123456789')
        outputs.append('abcdefghijklmnopqrstuvwxyz0123456789')
        outputs.append('....................................')
        outputs.append('')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_detaileddifferences.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
