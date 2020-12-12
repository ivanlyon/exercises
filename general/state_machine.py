"""
    State machine data structure with one start state and one stop state.

    Source: http://www.python-course.eu/finite_state_machine.php
"""

class InitializationError(ValueError): pass
class InputError(ValueError): pass

###############################################################################

class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.start = None # s
        self.end = None   # t

    def add_state(self, name, callback=None, start_state=False, end_state=False):
        name = name.upper()
        if name in self.handlers:
            raise InitializationError('unable to reassign state name "' + name + '"')
        self.handlers[name] = callback
        if end_state:
            self.end = name
        if start_state:
            self.start = name

    def set_start(self, name):
        self.start = name.upper()

    def set_end(self, name):
        self.end = name.upper()

    def run(self, cargo, start=None):
        run_start = self.start
        if start:
            run_start = start.upper()

        if None == run_start:
            raise InitializationError("assign start state before .run()")
        if not self.end:
            raise InitializationError("assign end state(s) before .run()")
        if not cargo or len(cargo) == 0:
            raise InputError("invalid fsm transitions supplied")

        try:
            handler = self.handlers[run_start]
        except:
            raise InitializationError("assign start state before .run()")

        #print(cargo)
        while True:
            (newState, cargo) = handler(cargo)
            #print("Reached", newState)
            if newState.upper() == self.end:
                break
            else:
                handler = self.handlers[newState.upper()]
                if not handler:
                    raise InputError("invalid fsm transitions supplied")

###############################################################################

if __name__ == '__main__':
    example = StateMachine()

    def parse_command(text, enclosures = '()'):
        lparen = text.find(enclosures[0])
        rparen = text.rfind(enclosures[1])
        return text[:lparen], text[lparen + 1: rparen]

    for lines in range(int(input().strip())):
        command, value = parse_command(input().strip())
        if command == 'add_state':
            example.add_state(value)
        elif command == 'set_start':
            example.set_start(value)
        elif command == 'set_end':
            example.set_end(value)
        elif command == 'print_state_machine':
            for h in example.handlers:
                print(str(h) + ' --> ' + str(example.handlers[h]))
            print('Start =', example.start)
            print('End =', example.end)
        else:
            print("Invalid command detected:", command)
