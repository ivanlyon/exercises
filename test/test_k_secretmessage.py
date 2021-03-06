import io
import unittest
from unittest.mock import patch
from kattis import k_secretmessage

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('iloveyoutooJill')
        inputs.append('TheContestisOver')
        inputs.append('iloveyouJack')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('iteiloylloooJuv')
        outputs.append('OsoTvtnheiterseC')
        outputs.append('Jeiaylcookuv')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_secretmessage.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
