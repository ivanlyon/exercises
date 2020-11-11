import unittest
from exercises import thread_fuzzing

###############################################################################

class TestThreadFuzzing(unittest.TestCase):
    '''
    Unittest class for the testing of the thread_fuzzing tutorial.
    '''

    def test_ordered_output(self):
        '''Test functions expected to produce ordered output.'''

        test_values = [5, 10]

        for t in test_values:
            valid_result = thread_fuzzing.get_results(t)
            self.assertEqual(valid_result, thread_fuzzing.get_results_function(t))
            self.assertEqual(valid_result, thread_fuzzing.get_results_function_threads(t))
            self.assertEqual(valid_result, thread_fuzzing.get_results_function_threads_fuzzed_locks(t))

    def test_unordered_output(self):
        '''Test functions expected to produce ordered output.'''

        self.assertNotEqual(thread_fuzzing.get_results(5), thread_fuzzing.get_results_function_threads_fuzzed(5))

###############################################################################

if __name__ == '__main__':
    unittest.main()
