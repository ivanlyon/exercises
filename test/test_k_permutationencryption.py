import io
import unittest
from unittest.mock import patch
from kattis import k_permutationencryption

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('1 1')
        inputs.append('Four score and seven years ago')
        inputs.append('2 2 1')
        inputs.append('our fathers brough forth on this continent a new nation,')
        inputs.append('5 1 3 2 5 4')
        inputs.append('conceived in liberty and dedicated to the proposition')
        inputs.append('10 5 10 8 1 3 6 4 7 2 9')
        inputs.append('that all men are created equal.')
        inputs.append('0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append("'Four score and seven years ago'")
        outputs.append("'uo rafhtre srbuohgf rohto  nhtsic noitentna n wen taoi,n'")
        outputs.append("'cnoeciev di nilbreyt na dddeciaet dt ohtep orpsotiino  '")
        outputs.append("' mltaatlh rece ea nr luaeedqta   .      '")
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_permutationencryption.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
