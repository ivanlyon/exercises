import unittest
from exercises import state_machine

###############################################################################

side_effects = []


class ValidTransitions(unittest.TestCase):
    '''
    Unittest with a simple 3 state model.

          '1'        '2'
     'a' -----> 'b' -----> 'c' (End state)
      |          |          |
      +----------+----------+--> bad_data

    '''

    def setUp(self):
        '''Clear the side effects list.'''
        global side_effects
        side_effects = []

    def a_state_transitions(text):
        '''Process data received while in state 'a'.'''
        global side_effects
        in_state = 'a'
        splitted_text = text.split(None, 1)
        word, text = splitted_text if len(splitted_text) > 1 else (text,'')
        if word == '1':
            next_state = 'b'
        else:
            next_state = 'bad_data'
        side_effects.append(in_state + ':' + next_state)
        return (next_state, text)

    def b_state_transitions(text):
        '''Process data received while in state 'b'.'''
        global side_effects
        in_state = 'b'
        splitted_text = text.split(None, 1)
        word, text = splitted_text if len(splitted_text) > 1 else (text,'')
        if word == '2':
            next_state = 'c'
        else:
            next_state = 'bad_data'
        side_effects.append(in_state + ':' + next_state)
        return (next_state, text)

    fsm = state_machine.StateMachine()
    fsm.add_state('a', callback=a_state_transitions, start_state = True)
    fsm.add_state('b', b_state_transitions)
    fsm.add_state('c', None, end_state = True)
    fsm.add_state('bad_data', None)

    def test_half_traversal(self):
        '''Test incomplete fsm data list never reaches end state.'''
        self.assertRaises(state_machine.InputError, self.fsm.run, '1')

    def test_full_traversal(self):
        '''Test complete fsm data list reaches end state.'''
        global side_effects
        self.fsm.run('1 2')
        self.assertEqual(' '.join(side_effects), 'a:b b:c')

        side_effects = []
        self.fsm.set_start('b')
        self.fsm.run('2')
        self.assertEqual(' '.join(side_effects), 'b:c')

        side_effects = []
        self.fsm.set_start('a')
        self.fsm.set_end('b')
        self.fsm.run('1')
        self.assertEqual(' '.join(side_effects), 'a:b')
        self.fsm.set_end('c')

        side_effects = []
        self.fsm.run('2', 'b')
        self.assertEqual(' '.join(side_effects), 'b:c')

    def test_beyond_full_traversal(self):
        '''Test data not received after fsm reaches end state.'''
        global side_effects
        self.fsm.run('1 2 3')
        self.assertEqual(' '.join(side_effects), 'a:b b:c')

    def test_bad_input(self):
        '''Test bad input at first state.'''
        self.assertRaises(state_machine.InputError, self.fsm.run, '2 1')

    def test_bad_add(self):
        '''Test invalid attempt to add an already existing state.'''
        self.assertRaises(state_machine.InitializationError, self.fsm.add_state, 'c')

###############################################################################

if __name__ == '__main__':
    unittest.main()
