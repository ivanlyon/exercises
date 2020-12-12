'''
Reference: Raymond Hettinger's Thinking In Threads presentation source.
'''

import threading, time, random, queue

FUZZ = True
DELAY_RANGE = 0.1  # maximum seconds per fuzz() when FUZZ == True
DIVIDER = '---------------'
START_LINE = 'Starting up'
FINISH_LINE = 'Finishing up'

###############################################################################

def fuzz():
    '''
    Fuzzing is a technique for amplifying race condition errors to make
    them more visible.
    '''
    if FUZZ:
        time.sleep(random.random() * DELAY_RANGE)

###############################################################################

def get_results(number):
    '''
    Start with working code that is clear, simple, and runs top to bottom.
    This is easy to develop and test incrementally.
    '''

    counter = 0
    result = START_LINE + '\n'

    for i in range(number):
        counter += 1
        result += 'The count is %02d' % counter
        result += '\n'
        result += DIVIDER
        result += '\n'

    return result + FINISH_LINE + '\n'

###############################################################################

def get_results_function(number):
    '''
    A next step in development is to factor re-usable code into functions.
    '''

    counter = 0
    result = START_LINE + '\n'

    def worker():
        'My job is to increment the counter and print the current count'

        nonlocal counter
        nonlocal result

        counter += 1
        result += 'The count is %02d' % counter
        result += '\n'
        result += DIVIDER
        result += '\n'

    for i in range(number):
        worker()

    return result + FINISH_LINE + '\n'

###############################################################################

def get_results_function_threads(number):
    '''
    Now with threading.
    '''

    counter = 0
    result = START_LINE + '\n'

    def worker():
        'My job is to increment the counter and print the current count'

        nonlocal counter
        nonlocal result

        counter += 1
        result += 'The count is %02d' % counter
        result += '\n'
        result += DIVIDER
        result += '\n'

    for i in range(number):
        threading.Thread(target=worker).start()

    return result + FINISH_LINE + '\n'

###############################################################################

def get_results_function_threads_fuzzed(number):
    '''
    Fuzzing is a technique for amplifying race conditions.
    '''

    counter = 0
    result = START_LINE + '\n'

    def worker():
        'My job is to increment the counter and print the current count'

        nonlocal counter
        nonlocal result

        fuzz()
        oldcnt = counter
        fuzz()
        counter = oldcnt + 1
        fuzz()
        result += 'The count is %02d' % counter
        fuzz()
        result += '\n'
        fuzz()
        result += DIVIDER
        fuzz()
        result += '\n'
        fuzz()

    fuzz()
    for i in range(number):
        threading.Thread(target=worker).start()
        fuzz()
    fuzz()

    return result + FINISH_LINE + '\n'

###############################################################################

def get_results_function_threads_fuzzed_locks(number):
    '''
    Atomic message queue to cure race conditions made obvious by fuzzing.
    To run without fuzzing, set the FUZZ variable to False.
    '''

    counter = 0
    counter_queue = queue.Queue()
    result = ''  # 'print'ed results accumulated

    def counter_manager():
        'I have EXCLUSIVE rights to update the counter variable'

        nonlocal counter
        nonlocal result

        while True:
            increment = counter_queue.get()
            fuzz()
            oldcnt = counter
            fuzz()
            counter = oldcnt + increment
            fuzz()
            result += 'The count is %02d' % counter
            fuzz()
            result += '\n'
            fuzz()
            result += DIVIDER
            fuzz()
            result += '\n'
            fuzz()
            counter_queue.task_done()

    t = threading.Thread(target=counter_manager)
    t.daemon = True
    t.start()
    del t

    print_queue = queue.Queue()

    def print_manager():
        'I have EXCLUSIVE rights to call the "print" keyword'

        nonlocal result

        while True:
            job = print_queue.get()
            fuzz()
            for line in job:
                result += line
                fuzz()
                result += '\n'
                fuzz()
            print_queue.task_done()
            fuzz()

    t = threading.Thread(target=print_manager)
    t.daemon = True
    t.start()
    del t

    def worker():
        'My job is to increment the counter and print the current count'
        counter_queue.put(1)
        fuzz()

    print_queue.put([START_LINE])
    fuzz()

    worker_threads = []
    for i in range(number):
        t = threading.Thread(target=worker)
        worker_threads.append(t)
        t.start()
        fuzz()
    for t in worker_threads:
        fuzz()
        t.join()

    counter_queue.join()
    fuzz()
    print_queue.put([FINISH_LINE])
    fuzz()
    print_queue.join()
    fuzz()

    return result

###############################################################################

if __name__ == '__main__':
    print(get_results(10))
    print(get_results_function(10))
    print(get_results_function_threads(10))
    print(get_results_function_threads_fuzzed(10))
    print(get_results_function_threads_fuzzed_locks(10))
