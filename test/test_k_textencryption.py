import io
import unittest
from unittest.mock import patch
from kattis import k_textencryption

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('CTU Open Programming Contest')
        inputs.append('7')
        inputs.append('This is a secret message that noone should ever see Lets encrypt it')
        inputs.append('15')
        inputs.append('text too short')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('CMTMUIONPGECNOPNRTOEGSRTA')
        outputs.append('TESNUECHCAOLERIRGODLYSEENEEPITTEVTTSMHSESIAEAHRETSSTOSN')
        outputs.append('TEXTTOOSHORT')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_textencryption.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
