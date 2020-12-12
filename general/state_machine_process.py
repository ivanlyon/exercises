'''
Finite State Machine algorithm used to assess score of Python found in
statements of the form 'Python is ___'.  The 2 possible scores are
'positive' and 'negative'.

Reference: http://www.python-course.eu/finite_state_machine.php

+--------------+-------------+--------------+
| From State   | Input       | To State     |
+--------------+-------------+--------------+
| Start        | 'Python'    | Python_state |
| Start        | Not handled | error_state  |
| Python_state | 'is'        | is_state     |
| Python_state | Not handled | error_state  |
| is_state     | {positive}  | pos_state    |
| is_state     | {negative}  | neg_state    |
| is_state     | 'not'       | not_state    |
| is_state     | Not handled | error_state  |
| not_state    | {positive}  | neg_state    |
| not_state    | {negative}  | pos_state    |
| not_state    | Not handled | error_state  |
| pos_state    | Any         | End          |
| neg_state    | Any         | End          |
| error_state  | Any         | End          |
+--------------+-------------+--------------+

Input:
------
    The first line contains a single integer for the number of test cases.
Each test case then appears on its own line as a word ('hex2dec' or 'dec2hex')
and a value to be converted.
  +------------------------------------------------------------------+
  | 3                                                                |
  | fsm_score('Python is great')                                     |
  | fsm_score('Python is difficult')                                 |
  | fsm_score('Perl is great')                                       |
  +------------------------------------------------------------------+

Output:
-------
    For each test case, the result will displayed on a line.
  +------------------------------------------------------------------+
  | fsm_score('Python is great') = positive                          |
  | fsm_score('Python is difficult') = negative                      |
  | fsm_score('Perl is great') = error                               |
  +------------------------------------------------------------------+
'''

from general import state_machine

POSITIVE_ADJECTIVES = []
NEGATIVE_ADJECTIVES = []

IS_STATE = 'is_state'
PYTHON_STATE = 'Python_state'
START_STATE = 'Start'
ERROR_STATE = 'error_state'
NOT_STATE = 'not_state'
POS_STATE = 'pos_state'
NEG_STATE = 'neg_state'
END_STATE = 'End'

SENTIMENT = ''

###############################################################################

def start_transitions(text):
    '''Perform transition at the state designated as start.'''
    splitted_text = text.split(None, 1)
    word, text = splitted_text if len(splitted_text) > 1 else (text,'')
    if word == "Python":
        newState = PYTHON_STATE
    else:
        newState = ERROR_STATE
        global SENTIMENT
        SENTIMENT = process_sentiment(ERROR_STATE)

    return (newState, text)

###############################################################################

def python_state_transitions(text):
    '''Perform transition from state designated by last transition "Python".'''
    splitted_text = text.split(None, 1)
    word, text = splitted_text if len(splitted_text) > 1 else (text,'')
    if word == "is":
        newState = IS_STATE
    else:
        newState = ERROR_STATE
        global SENTIMENT
        SENTIMENT = process_sentiment(ERROR_STATE)

    return (newState, text)

###############################################################################

def is_state_transitions(text):
    '''Perform transition from state designated by last transition "is".'''
    splitted_text = text.split(None, 1)
    word, text = splitted_text if len(splitted_text) > 1 else (text,'')
    if word == "not":
        newState = NOT_STATE
    else:
        if word in POSITIVE_ADJECTIVES:
            newState = POS_STATE
        elif word in NEGATIVE_ADJECTIVES:
            newState = NEG_STATE
        else:
            newState = ERROR_STATE

        global SENTIMENT
        SENTIMENT = process_sentiment(newState)

    return (newState, text)

###############################################################################

def not_state_transitions(text):
    '''Perform transition from state designated by last transition "not".'''
    splitted_text = text.split(None, 1)
    word, text = splitted_text if len(splitted_text) > 1 else (text,'')
    if word in POSITIVE_ADJECTIVES:
        newState = NEG_STATE
    elif word in NEGATIVE_ADJECTIVES:
        newState = POS_STATE
    else:
        newState = ERROR_STATE

    global SENTIMENT
    SENTIMENT = process_sentiment(newState)

    return (newState, text)

###############################################################################

def final_transitions(text):
    '''Perform transition from any state to designated end state.'''
    return (END_STATE, text)

###############################################################################

def process_sentiment(text):
    '''Compute sentiment from resolved state identifier.'''
    if text == POS_STATE: result = 'positive'
    elif text == NEG_STATE: result = 'negative'
    else: result = 'error'
    return result

###############################################################################

fsm = state_machine.StateMachine()
fsm.add_state(START_STATE, start_transitions)
fsm.add_state(PYTHON_STATE, python_state_transitions)
fsm.add_state(IS_STATE, is_state_transitions)
fsm.add_state(NOT_STATE, not_state_transitions)
fsm.add_state(NEG_STATE, final_transitions)
fsm.add_state(POS_STATE, final_transitions)
fsm.add_state(ERROR_STATE, final_transitions)
fsm.add_state(END_STATE, None)
fsm.set_start(START_STATE)
fsm.set_end(END_STATE)

if __name__== "__main__":
    def parse_command(text, enclosures = '()'):
        lparen = text.find(enclosures[0])
        rparen = text.rfind(enclosures[1])
        return text[:lparen], text[lparen + 1: rparen]

    for line in range(int(input())):
        command, value = parse_command(input().strip())
        if command == 'ADD_POSITIVE':
            POSITIVE_ADJECTIVES.append(eval(value))
        elif command == 'ADD_NEGATIVE':
            NEGATIVE_ADJECTIVES.append(eval(value))
        elif command == 'RUN':
            fsm.run(eval(value))
            print(SENTIMENT)
