import io
import unittest
from unittest.mock import patch
from kattis import k_recipes

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('2')
        inputs.append('6 4 20')
        inputs.append('oliveoil 50.9 11.2')
        inputs.append('garlic 12.0 2.7')
        inputs.append('beef 453.6 100.0')
        inputs.append('onions 1134.0 250.0')
        inputs.append('raisins 82.5 18.2')
        inputs.append('bouillon 10.0 2.2')
        inputs.append('4 5 8')
        inputs.append('Milk 265.0 93.0')
        inputs.append('SodiumCitrate 11.0 4.0')
        inputs.append('WhiteCheddar 285.0 100.0')
        inputs.append('DryMacaroni 240.0 84.0')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('Recipe # 1')
        outputs.append('oliveoil 254.0')
        outputs.append('garlic 61.2')
        outputs.append('beef 2268.0')
        outputs.append('onions 5670.0')
        outputs.append('raisins 412.8')
        outputs.append('bouillon 49.9')
        outputs.append('----------------------------------------')
        outputs.append('Recipe # 2')
        outputs.append('Milk 424.1')
        outputs.append('SodiumCitrate 18.2')
        outputs.append('WhiteCheddar 456.0')
        outputs.append('DryMacaroni 383.0')
        outputs.append('----------------------------------------')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_recipes.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
