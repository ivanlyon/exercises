import unittest
from exercises import logging_screen

###############################################################################

class TestLoggingScreen(unittest.TestCase):
    '''
    Unittest class for the testing of the logging_screen exercises.
    '''

    def test_log_to_string(self):
        '''Test functions expected to produce log messages.'''

        logger = logging_screen.log_to_string_configure()
        logger.debug('debug test')
        self.assertEqual('debug test\n', logging_screen.LOG_CAPTURE_STRING.getvalue())

        logger = logging_screen.log_to_string_configure()
        logger.info('info test')
        self.assertEqual('info test\n', logging_screen.LOG_CAPTURE_STRING.getvalue())

        logger = logging_screen.log_to_string_configure()
        logger.warning('warning test')
        self.assertEqual('warning test\n', logging_screen.LOG_CAPTURE_STRING.getvalue())

        logger = logging_screen.log_to_string_configure()
        logger.error('error test')
        self.assertEqual('error test\n', logging_screen.LOG_CAPTURE_STRING.getvalue())

        logger = logging_screen.log_to_string_configure()
        logger.critical('critical test')
        self.assertEqual('critical test\n', logging_screen.LOG_CAPTURE_STRING.getvalue())

###############################################################################

if __name__ == '__main__':
    unittest.main()
