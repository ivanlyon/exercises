import io
import unittest
from unittest.mock import patch
from kattis import k_hardwoodspecies

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = '''
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
'''

        outputs = '''
Ash 13.793103
Aspen 3.448276
Basswood 3.448276
Beech 3.448276
Black Walnut 3.448276
Cherry 3.448276
Cottonwood 3.448276
Cypress 3.448276
Gum 3.448276
Hackberry 3.448276
Hard Maple 3.448276
Hickory 3.448276
Pecan 3.448276
Poplan 3.448276
Red Alder 3.448276
Red Elm 3.448276
Red Oak 6.896552
Sassafras 3.448276
Soft Maple 3.448276
Sycamore 3.448276
White Oak 10.344828
Willow 3.448276
Yellow Birch 3.448276
'''

        with patch('sys.stdin', io.StringIO(inputs[1:])) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_hardwoodspecies.main()
            self.assertEqual(stdout.getvalue(), outputs[1:])
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
