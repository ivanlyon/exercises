#!/usr/bin/python3
'''
Convex Hull computation plus optional plotted demonstration. Note main2()
provided for "Accepted" submission for Kattis/convexhull2.

Status: Accepted
'''

###############################################################################

class Point():
    '''Data and operations of 2D points'''

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __le__(self, other):
        return self < other or self == other

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

###############################################################################

class Line():
    '''Data and operations of 2D lines'''

    def __init__(self, pt_p, pt_q):
        self.pt_p, self.pt_q = pt_p, pt_q

    def __repr__(self):
        return '[' + str(self.pt_p) + '->' + str(self.pt_q) + ']'

    def distance2(self):
        '''Return square of distance of line segment.'''
        xdelta = self.pt_p.x - self.pt_q.x
        ydelta = self.pt_p.y - self.pt_q.y
        return xdelta * xdelta + ydelta * ydelta

###############################################################################

def signed_triangle_area(pt_a, pt_b, pt_c):
    '''Area of triangle is positive when a->b->c is ccw.'''
    return 0.5 * (pt_a.x * pt_b.y - pt_a.y * pt_b.x + pt_a.y * pt_c.x -
                  pt_a.x * pt_c.y + pt_b.x * pt_c.y - pt_c.x * pt_b.y)

def xvector(origin, pt_a, pt_b):
    '''Cross product of vectors OA and OB. Result > 0 for CCW.'''
    return (pt_a.x - origin.x) * (pt_b.y - origin.y) - \
           (pt_a.y - origin.y) * (pt_b.x - origin.x)

###############################################################################

class ConvexHull():
    '''Convex Hull setup and computation.'''

    def __init__(self, collinear=False, polygon=False):
        self._points = []
        self._hull_points = []
        self._collinear = collinear # True for collinear points in result
        self._polygon = polygon     # True for 1st == last of result

    def add1(self, x_coord, y_coord):
        '''Add 1 point for consideration in future convex hull creation.'''
        self._hull_points = []
        self._points.append(Point(x_coord, y_coord))

    def set_points(self, pairs):
        '''Assign all data points at once.'''
        self._hull_points = []
        self._points = []
        for pair in pairs:
            self.add1(pair[0], pair[1])

    def compute_hull(self):
        '''Need relative angle sort of points'''
        points = sorted(set(self._points))
        if len(points) < 3:
            self._hull_points = points
            return

        lower = []
        upper = []

        if self._collinear:
            for point in points:
                while len(lower) >= 2 and xvector(lower[-2], lower[-1], point) < 0:
                    lower.pop()
                lower.append(point)

            for point in reversed(points):
                while len(upper) >= 2 and xvector(upper[-2], upper[-1], point) < 0:
                    upper.pop()
                upper.append(point)
        else:
            for point in points:
                while len(lower) >= 2 and xvector(lower[-2], lower[-1], point) <= 0:
                    lower.pop()
                lower.append(point)

            for point in reversed(points):
                while len(upper) >= 2 and xvector(upper[-2], upper[-1], point) <= 0:
                    upper.pop()
                upper.append(point)

        self._hull_points = lower[:-1] + upper[:-1]
        if self._polygon:
            self._hull_points.append(self._hull_points[0])

    def get_hull_points(self):
        '''Return convex hull of points. Create convex hull on miss.'''
        if not self._hull_points:
            self.compute_hull()

        return self._hull_points

    def get_hull_ints(self):
        '''Return convex hull of int coords. Create convex hull on miss.'''
        self.get_hull_points()
        result = []
        for point in self._hull_points:
            result.append([point.x, point.y])

        return result

    def demonstration(self):
        '''Plot points and convex hull for demonstration.'''
        import matplotlib.pyplot as plt

        # Console result
        pt_hull = self.get_hull_points()
        print('Hull of ' + str(len(self._points)) +
              ' random points produces convex hull polygon of ' +
              str(len(pt_hull) - 1) + ' points: ' + str(pt_hull))

        # Plot result
        plt.figure('Convex Hull Demo')
        x_coord = [pt_random.x for pt_random in self._points]
        y_coord = [pt_random.y for pt_random in self._points]
        plt.scatter(x_coord, y_coord, marker='o')

        chx = [pt_chull.x for pt_chull in self._hull_points]
        chy = [pt_chull.y for pt_chull in self._hull_points]
        plt.plot(chx, chy, marker='D', color='red', linestyle='dashed')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.suptitle('Convex Hull Demonstration')
        plt.title(str(len(x_coord)) + ' Random Points')

        plt.show()

###############################################################################

def demo():
    '''Convex Hull demonstration with plotted outputs.'''
    import random

    chull = ConvexHull(collinear=True, polygon=True)
    lo_val = -100
    hi_val = 100
    for _ in range(random.randint(40, 60)):
        chull.add1(random.randint(lo_val, hi_val), random.randint(lo_val, hi_val))

    chull.demonstration()

###############################################################################

def main2():
    '''Function to call when using input of Kattis convexhull2.'''
    chull = ConvexHull(collinear=True)
    for _ in range(int(input())):
        x_coord, y_coord, on_chull = input().split()
        if on_chull == 'Y':
            chull.add1(int(x_coord), int(y_coord))
    result = chull.get_hull_points()
    print(str(len(result)))
    for pt_r in result:
        print(str(pt_r.x), str(pt_r.y))

###############################################################################

def main():
    '''Convex Hull computation of points received as formatted input'''
    while 1:
        points = int(input())
        if points == 0:
            break

        chull = ConvexHull()
        for _ in range(points):
#            x, y = [int(a) for a in input().split()]
#            chull.add1(x, y)
            chull.add1(*[int(a) for a in input().split()])

        results = chull.get_hull_points()
        print(str(len(results)))
        for pt_r in results:
            print(str(pt_r.x), str(pt_r.y))

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="convex hull demonstration", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
