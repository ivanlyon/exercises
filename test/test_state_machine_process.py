import unittest
from exercises import state_machine_process

###############################################################################

class ValidTransitions(unittest.TestCase):
    '''
    Unittest model of FSM representation for the sentiment computation of
    'Python is [not] {modifier}' statements.

                                        ------> State 4 ---->+
                                       /         /|\         |
                                   {+}/        {-}|          |
                                     /            |          |
           'Python'        'is'     /    'not'    |         \|/
     State 0 ----> State 1 ----> State 2 ----> State 3     End
                                    \             |         /|\
                                     \            |          |
                                   {-}\        {+}|          |
                                       \         \|/         |
                                        ------> State 5 ---->+
    '''

    def test_positive(self):
        '''Test positive sentiment result.'''
        state_machine_process.POSITIVE_ADJECTIVES.append('great')
        state_machine_process.POSITIVE_ADJECTIVES.append('super')
        state_machine_process.POSITIVE_ADJECTIVES.append('easy')
        state_machine_process.fsm.run('Python is great')
        self.assertEqual(state_machine_process.SENTIMENT, 'positive')
        state_machine_process.fsm.run('Python is easy')
        self.assertEqual(state_machine_process.SENTIMENT, 'positive')

    def test_negative(self):
        '''Test negative sentiment result.'''
        state_machine_process.NEGATIVE_ADJECTIVES.append('boring')
        state_machine_process.NEGATIVE_ADJECTIVES.append('bad')
        state_machine_process.fsm.run('Python is boring')
        self.assertEqual(state_machine_process.SENTIMENT, 'negative')
        state_machine_process.fsm.run('Python is bad')
        self.assertEqual(state_machine_process.SENTIMENT, 'negative')

    def test_not(self):
        '''Test sentiment negation.'''
        state_machine_process.POSITIVE_ADJECTIVES.append('fun')
        state_machine_process.POSITIVE_ADJECTIVES.append('entertaining')
        state_machine_process.NEGATIVE_ADJECTIVES.append('difficult')
        state_machine_process.NEGATIVE_ADJECTIVES.append('ugly')
        state_machine_process.fsm.run('Python is not fun')
        self.assertEqual(state_machine_process.SENTIMENT, 'negative')
        state_machine_process.fsm.run('Python is not entertaining')
        self.assertEqual(state_machine_process.SENTIMENT, 'negative')
        state_machine_process.fsm.run('Python is not difficult')
        self.assertEqual(state_machine_process.SENTIMENT, 'positive')
        state_machine_process.fsm.run('Python is not ugly')
        self.assertEqual(state_machine_process.SENTIMENT, 'positive')

    def test_error(self):
        '''Test error result when incompatible input is processed.'''
        state_machine_process.fsm.run('Perl is not fun')
        self.assertEqual(state_machine_process.SENTIMENT, 'error')
        state_machine_process.fsm.run('Python rocks')
        self.assertEqual(state_machine_process.SENTIMENT, 'error')
        state_machine_process.fsm.run('Python is ineffable')
        self.assertEqual(state_machine_process.SENTIMENT, 'error')
        state_machine_process.fsm.run('Python is not ineffable')
        self.assertEqual(state_machine_process.SENTIMENT, 'error')

###############################################################################

if __name__ == '__main__':
    unittest.main()
