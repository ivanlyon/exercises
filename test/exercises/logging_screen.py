'''
Illustrative examples for using Python's logging module to print leveled
comments to console.
'''

import importlib
import io
import logging
import logging.config
import os
import sys

LOG_CAPTURE_STRING = io.StringIO()

###############################################################################

def method_configure():
    'configure logger using library methods'
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

#    handler = logging.StreamHandler()  # stderr by default
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger = logging.getLogger('console_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger

###############################################################################

def log_to_string_configure():
    global LOG_CAPTURE_STRING
    LOG_CAPTURE_STRING = io.StringIO()

    'configure logger using library methods'

    handler = logging.StreamHandler(LOG_CAPTURE_STRING)
    handler.setLevel(logging.DEBUG)

    logger = logging.getLogger('string_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger

###############################################################################

def one_of_each_level(logger):
    'invoke each logging level message to confirm configured appearances'
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

###############################################################################

def print_title(text):
    'utility function to show line of text followed by an underline.'
    print(text)
    print('-' * len(text))

###############################################################################

def configuration_file(create):
    'configure logger using a configuration file.'
    filename = 'logging.conf'
    if create:
        # Reference: https://docs.python.org/3/howto/logging.html
        text = '''
            [loggers]
            keys=root,simpleExample

            [handlers]
            keys=screen

            [formatters]
            keys=simple,complex

            [logger_root]
            level=NOTSET
            handlers=screen

            [logger_simpleExample]
            level=DEBUG
            handlers=screen
            qualname=simpleExample
            propagate=0

            [handler_screen]
            class=StreamHandler
            level=DEBUG
            formatter=complex
            args=(sys.stdout,)

            [formatter_simple]
            format=%(asctime)s - %(levelname)s - %(message)s
            datefmt=

            [formatter_complex]
            format=%(asctime)s - %(levelname)-8s - <%(module)s: %(lineno)d> - %(message)s
            datefmt=
        '''
        with open(filename, 'w') as conf_file:
            conf_file.write(text)
        logging.config.fileConfig(filename)
        logger = logging.getLogger('fileConfigExample')
    else:
        os.remove(filename)

###############################################################################

if __name__ == '__main__':
    importlib.reload(logging)
    print_title("In-Line basic configuration:")
#    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)-8s - %(message)s')
    logging.basicConfig(stream=sys.stdout,level=logging.DEBUG,format='%(asctime)s - %(levelname)-8s - %(message)s')
    one_of_each_level(logging.getLogger())
    print()
    importlib.reload(logging)
    print_title("Method Configuration:")
    one_of_each_level(method_configure())
    print()
    importlib.reload(logging)
    print_title("Logging to String Configuration:")
    one_of_each_level(log_to_string_configure())
    print(LOG_CAPTURE_STRING.getvalue())
    importlib.reload(logging)
    configuration_file(True)
    print_title("File Configuration:")
    one_of_each_level(logging.getLogger('fileConfigExample'))
    configuration_file(False)
    print()
    importlib.reload(logging)
    print_title("Default configuration:")
    one_of_each_level(logging.getLogger())
