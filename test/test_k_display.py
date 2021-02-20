import io
import unittest
from unittest.mock import patch
from kattis import k_display

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input(self):
        '''Run and assert problem statement sample input and output.'''
        inputs = []
        inputs.append('16:47')
        inputs.append('23:59')
        inputs.append('00:08')
        inputs.append('end')
        inputs = '\n'.join(inputs) + '\n'

        outputs = []
        outputs.append('    +  +---+     +   +  +---+')
        outputs.append('    |  |         |   |      |')
        outputs.append('    |  |      o  |   |      |')
        outputs.append('    +  +---+     +---+      +')
        outputs.append('    |  |   |  o      |      |')
        outputs.append('    |  |   |         |      |')
        outputs.append('    +  +---+         +      +')
        outputs.append('')
        outputs.append('')
        outputs.append('+---+  +---+     +---+  +---+')
        outputs.append('    |      |     |      |   |')
        outputs.append('    |      |  o  |      |   |')
        outputs.append('+---+  +---+     +---+  +---+')
        outputs.append('|          |  o      |      |')
        outputs.append('|          |         |      |')
        outputs.append('+---+  +---+     +---+  +---+')
        outputs.append('')
        outputs.append('')
        outputs.append('+---+  +---+     +---+  +---+')
        outputs.append('|   |  |   |     |   |  |   |')
        outputs.append('|   |  |   |  o  |   |  |   |')
        outputs.append('+   +  +   +     +   +  +---+')
        outputs.append('|   |  |   |  o  |   |  |   |')
        outputs.append('|   |  |   |     |   |  |   |')
        outputs.append('+---+  +---+     +---+  +---+')
        outputs.append('')
        outputs.append('')
        outputs.append('end')
        outputs = '\n'.join(outputs) + '\n'

        self.maxDiff = None
        with patch('sys.stdin', io.StringIO(inputs)) as stdin,\
             patch('sys.stdout', new_callable=io.StringIO) as stdout:
            k_display.main()
            self.assertEqual(stdout.getvalue(), outputs)
            self.assertEqual(stdin.read(), '')

###############################################################################

if __name__ == '__main__':
    unittest.main()
