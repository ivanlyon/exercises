import io
import unittest
from unittest.mock import patch
from kattis import k_piglatin

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''
        inputs = 'i cant speak pig latin\n'
        outputs = 'iyay antcay eakspay igpay atinlay\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_piglatin.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''
        inputs = []
        inputs.append('the quick brown fox')
        inputs.append('jumps over the lazy dog')
        inputs.append('and ordinary foxes')
        inputs.append('dont jump over lazy dogs')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('ethay uickqay ownbray oxfay')
        outputs.append('umpsjay overyay ethay azylay ogday')
        outputs.append('andyay ordinaryyay oxesfay')
        outputs.append('ontday umpjay overyay azylay ogsday')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_piglatin.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
