import io
import unittest
from unittest.mock import patch
from kattis import k_solitaire

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('###...###')
        inputs.append('..oo.....')
        inputs.append('.....oo..')
        inputs.append('.........')
        inputs.append('###...###')
        inputs.append('')
        inputs.append('###...###')
        inputs.append('..oo.o...')
        inputs.append('...o.oo..')
        inputs.append('...oo....')
        inputs.append('###...###')
        inputs.append('')
        inputs.append('###o..###')
        inputs.append('.o.oo....')
        inputs.append('o.o......')
        inputs.append('.o.o.....')
        inputs.append('###...###')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('1 3')
        outputs.append('1 7')
        outputs.append('1 7')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_solitaire.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

    def test_zeroes(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('3')
        inputs.append('###...###')
        inputs.append('.........')
        inputs.append('.........')
        inputs.append('.........')
        inputs.append('###...###')
        inputs.append('')
        inputs.append('###...##')
        inputs.append('..o....')
        inputs.append('.o....')
        inputs.append('.....')
        inputs.append('####')
        inputs.append('')
        inputs.append('###...##')
        inputs.append('..oo...')
        inputs.append('.o..o.')
        inputs.append('.....')
        inputs.append('####')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('0 0')
        outputs.append('2 0')
        outputs.append('2 2')
        outputs = '\n'.join(outputs) + '\n'

        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_solitaire.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
