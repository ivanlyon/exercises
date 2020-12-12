'''
Reference: http://redclay.altervista.org/wiki/doku.php?id=projects:python-threading

Variations of resource access control for python threads.
'''

import threading
import queue
import time
import random

OUTPUT_TEXT = ''
SENTINEL = 'THE_END'

###############################################################################

def queue_condition_empty(productions):
    '''
    Handle empty queue using Condition.
    '''

    global OUTPUT_TEXT
    OUTPUT_TEXT = ''

    resource = []
    condition = threading.Condition()

    def producer(productions):
        'produce a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            number = random.randint(0, 1000)
            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} produced {}\n'.format(
                current_thread.getName(),
                str(number).zfill(3))

            condition.acquire()
            resource.append(number)
            condition.notify()
            condition.release()

    def consumer(productions):
        'consume a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            condition.acquire()
            if not resource:
                condition.wait()
            consuming = resource.pop()
            condition.release()

            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} consumed {}\n'.format(
                current_thread.getName(),
                str(consuming).zfill(3))

        OUTPUT_TEXT += SENTINEL

    t_producer = threading.Thread(name='Producer',
                                  target=producer,
                                  args=(productions,))
    t_consumer = threading.Thread(name='Consumer',
                                  target=consumer,
                                  args=(productions,))

    t_producer.start()
    t_consumer.start()

###############################################################################

def queue_semaphore_empty(productions):
    '''
    Handle empty queue using Semaphore.
    '''

    global OUTPUT_TEXT
    OUTPUT_TEXT = ''

    resource = []
    sema4 = threading.Semaphore(value=0)
    thread_lock = threading.Lock()

    def producer(productions):
        'produce a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            number = random.randint(0, 1000)
            time.sleep(random.uniform(0, 1))  # Process time simulation

            thread_lock.acquire()
            sema4.release()
            resource.append(number)
            OUTPUT_TEXT += '{} produced {}, semaphore = {}\n'.format(
                current_thread.getName(),
                str(number).zfill(3),
                str(sema4._value))
            thread_lock.release()

    def consumer(productions):
        'consume a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            sema4.acquire()
            thread_lock.acquire()
            consuming = resource.pop()
            OUTPUT_TEXT += '{} consumed {}, semaphore = {}\n'.format(
                current_thread.getName(),
                str(consuming).zfill(3),
                str(sema4._value))
            thread_lock.release()

            time.sleep(random.uniform(0, 1))  # Process time simulation

        OUTPUT_TEXT += SENTINEL

    t_producer = threading.Thread(name='Producer',
                                  target=producer,
                                  args=(productions,))
    t_consumer = threading.Thread(name='Consumer',
                                  target=consumer,
                                  args=(productions,))

    t_producer.start()
    t_consumer.start()

###############################################################################

def queue_event_empty_full(productions):
    '''
    Handle empy and full queue using Event.
    '''

    global OUTPUT_TEXT
    OUTPUT_TEXT = ''

    resource = []
    bandwidth = 5

    lock = threading.Lock()
    event_full = threading.Event()
    event_empty = threading.Event()

    def producer(productions):
        'produce a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            number = random.randint(0, 1000)
            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} produced {}\n'.format(current_thread.getName(),
                                                     str(number).zfill(3))

            lock.acquire()
            if len(resource) >= bandwidth:
                event_full.clear()
                lock.release()
                event_full.wait()
                lock.acquire()
            resource.append(number)
            if not event_empty.isSet():
                event_empty.set()
            lock.release()

    def consumer(productions):
        'consume a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            lock.acquire()
            if not resource:
                event_empty.clear()
                lock.release()
                event_empty.wait()
                lock.acquire()
            consuming = resource.pop()
            if not event_full.isSet():
                event_full.set()
            lock.release()

            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} consumed {}\n'.format(current_thread.getName(),
                                                     str(consuming).zfill(3))

        OUTPUT_TEXT += SENTINEL

    t_producer = threading.Thread(name='Producer',
                                  target=producer,
                                  args=(productions,))
    t_consumer = threading.Thread(name='Consumer',
                                  target=consumer,
                                  args=(productions,))

    t_producer.start()
    t_consumer.start()

###############################################################################

def queue_empty_full(productions):
    '''
    Handle empty and full queue using Queue.
    '''

    global OUTPUT_TEXT
    OUTPUT_TEXT = ''

    bandwidth = 5
    resource = queue.Queue(bandwidth)

    def producer(productions):
        'produce a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            number = random.randint(0, 1000)
            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} produced {}\n'.format(current_thread.getName(),
                                                     str(number).zfill(3))
            resource.put(number)

    def consumer(productions):
        'consume a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            consuming = resource.get()
            time.sleep(random.uniform(0, 1))
            OUTPUT_TEXT += '{} consumed {}\n'.format(current_thread.getName(),
                                                     str(consuming).zfill(3))

        OUTPUT_TEXT += SENTINEL

    t_producer = threading.Thread(name='Producer',
                                  target=producer,
                                  args=(productions,))
    t_consumer = threading.Thread(name='Consumer',
                                  target=consumer,
                                  args=(productions,))

    t_producer.start()
    t_consumer.start()

###############################################################################

def queue_bounded_semaphore(productions):
    '''
    Handle empty and full queue using Queue.
    '''

    global OUTPUT_TEXT
    OUTPUT_TEXT = ''

    resource = []
    bandwidth = 2

    lock = threading.Lock()
    sema4 = threading.BoundedSemaphore(value=bandwidth)

    def producer(productions):
        'produce a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            number = random.randint(0, 1000)
            time.sleep(random.uniform(0, 0.5))

            sema4.acquire()
            lock.acquire()
            resource.append(number)
            lock.release()
            OUTPUT_TEXT += '{} produced {}, semaphore = {}\n'.format(
                current_thread.getName(),
                str(number).zfill(3),
                str(sema4._value))

    def consumer(productions):
        'consume a fixed number of items'
        global OUTPUT_TEXT

        current_thread = threading.currentThread()
        for _ in range(productions):
            # TODO: find better way
            while resource == []:
                time.sleep(.1)

            lock.acquire()
            consuming = resource.pop()
            lock.release()
            sema4.release()

            OUTPUT_TEXT += '{} consumed {}, semaphore = {}\n'.format(
                current_thread.getName(),
                str(consuming).zfill(3),
                str(sema4._value))
            time.sleep(random.uniform(0, 1))

        OUTPUT_TEXT += SENTINEL

    t_producer = threading.Thread(name='Producer',
                                  target=producer,
                                  args=(productions,))
    t_consumer = threading.Thread(name='Consumer',
                                  target=consumer,
                                  args=(productions,))

    t_producer.start()
    t_consumer.start()

###############################################################################

if __name__ == '__main__':
    print('queue_condition_empty:')
    queue_condition_empty(10)
    while not OUTPUT_TEXT.endswith(SENTINEL):
        time.sleep(.1)
    print(OUTPUT_TEXT[:-len(SENTINEL)], end='')
    print()
    print('queue_semaphore_empty:')
    queue_semaphore_empty(10)
    while not OUTPUT_TEXT.endswith(SENTINEL):
        time.sleep(.1)
    print(OUTPUT_TEXT[:-len(SENTINEL)], end='')
    print()
    print('queue_event_empty_full:')
    queue_event_empty_full(10)
    while not OUTPUT_TEXT.endswith(SENTINEL):
        time.sleep(.1)
    print(OUTPUT_TEXT[:-len(SENTINEL)], end='')
    print()
    print('queue_empty_full:')
    queue_empty_full(10)
    while not OUTPUT_TEXT.endswith(SENTINEL):
        time.sleep(.1)
    print(OUTPUT_TEXT[:-len(SENTINEL)], end='')
    print()
    print('queue_bounded_semaphore:')
    queue_bounded_semaphore(10)
    while not OUTPUT_TEXT.endswith(SENTINEL):
        time.sleep(.1)
    print(OUTPUT_TEXT[:-len(SENTINEL)], end='')
