import io
import unittest
from unittest.mock import patch
from kattis import k_catenyms

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('6')
        inputs.append('aloha')
        inputs.append('arachnid')
        inputs.append('dog')
        inputs.append('gopher')
        inputs.append('rat')
        inputs.append('tiger')
        inputs.append('3')
        inputs.append('oak')
        inputs.append('maple')
        inputs.append('elm')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('aloha.arachnid.dog.gopher.rat.tiger')
        outputs.append('***')
        outputs = '\n'.join(outputs) + '\n'
        self.maxDiff = None
        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_catenyms.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_custom_cases(self):
        '''Run and assert custom test cases.'''
        inputs = []
        inputs.append('4')
        inputs.append('5')
        inputs.append('aloha')
        inputs.append('arachnid')
        inputs.append('alpha')
        inputs.append('dud')
        inputs.append('donna')
        inputs.append('3')
        inputs.append('maple')
        inputs.append('elm')
        inputs.append('elle')
        inputs.append('3')
        inputs.append('ends')
        inputs.append('sends')
        inputs.append('rends')
        inputs.append('4')
        inputs.append('maple')
        inputs.append('staple')
        inputs.append('elle')
        inputs.append('elke')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('aloha.alpha.arachnid.dud.donna')
        outputs.append('elle.elm.maple')
        outputs.append('***')
        outputs.append('***')
        outputs = '\n'.join(outputs) + '\n'
        self.maxDiff = None
        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_catenyms.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
