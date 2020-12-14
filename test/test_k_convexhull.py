import unittest
from kattis import k_convexhull

###############################################################################

class SampleInput(unittest.TestCase):
    '''Problem statement sample inputs and outputs'''

    def test_sample_input_1(self):
        '''Run and assert problem statement sample 1 input and output.'''

        points = []
        points.append([0, 0])
        points.append([10, 0])
        points.append([0, 10])

        ch = k_convexhull.ConvexHull()
        ch.set_points(points)
        self.assertEqual(ch.get_hull_ints(), points)

    def test_sample_input_2(self):
        '''Run and assert problem statement sample 2 input and output.'''

        points = []
        points.append([41, -6])
        points.append([-24, -74])
        points.append([-51, -6])
        points.append([73, 17])
        points.append([-30, -34])

        expected_results = []
        expected_results.append([-51, -6])
        expected_results.append([-24, -74])
        expected_results.append([73, 17])

        ch = k_convexhull.ConvexHull()
        ch.set_points(points)
        self.assertEqual(ch.get_hull_ints(), expected_results)

    def test_sample_input_3(self):
        '''Run and assert problem statement sample 3 input and output.'''

        points = []
        points.append([50, 50])
        points.append([50, 50])

        expected_results = []
        expected_results.append([50, 50])

        ch = k_convexhull.ConvexHull()
        ch.set_points(points)
        self.assertEqual(ch.get_hull_ints(), expected_results)

###############################################################################

if __name__ == '__main__':
    unittest.main()
