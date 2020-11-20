#!/usr/bin/python3
'''
Convex Hull computation plus optional plotted demonstration. Note main2()
provided for "Accepted" submission for Kattis/convexhull2.

Status: Accepted
'''

import sys

###############################################################################

class Point(object):
    '''Data and operations of 2D points'''

    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
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

class Line(object):
    '''Data and operations of 2D lines'''

    def __init__(self, p, q):
        self.p, self.q = p, q
    
    def __repr__(self):
        return '[' + str(p) + '->' + str(q) + ']'

    def distance2(self):
        '''Return square of distance of line segment.'''
        dx = self.p.x - self.q.x
        dy = self.p.y - self.q.y
        return dx * dx + dy * dy

###############################################################################

def signedTriangleArea(a, b, c):
    '''Area of triangle is positive when a->b->c is ccw.'''
    return 0.5 * (a.x * b.y - a.y * b.x + a.y * c.x - a.x * c.y + b.x * c.y - c.x * b.y);

def xvector(origin, a, b):
    '''Cross product of vectors OA and OB. Result > 0 for CCW.'''
    return (a.x - origin.x) * (b.y - origin.y) - \
           (a.y - origin.y) * (b.x - origin.x)

###############################################################################

class ConvexHull(object):
    '''Convex Hull setup and computation.'''

    def __init__(self, collinear = False, polygon = False):
        self._points = []
        self._hull_points = []
        self._collinear = collinear # True for collinear points in result
        self._polygon = polygon     # True for 1st == last of result

    def add1(self, x, y):
        '''Add 1 point for consideration in future convex hull creation.'''
        self._hull_points = []
        self._points.append(Point(x, y))

    def setPoints(self, pairs):
        '''Assign all data points at once.'''
        self._hull_points = []
        self._points = []
        for p in pairs:
            self.add1(p[0], p[1])

    def compute_hull(self):
        '''Need relative angle sort of points'''
        points = sorted(set(self._points))
        if len(points) < 3:
            self._hull_points = points
            return

        lower = []
        upper = []

        if self._collinear:
            for p in points:
                while len(lower) >= 2 and xvector(lower[-2], lower[-1], p) < 0:
                    lower.pop()
                lower.append(p)

            for p in reversed(points):
                while len(upper) >= 2 and xvector(upper[-2], upper[-1], p) < 0:
                    upper.pop()
                upper.append(p)
        else:
            for p in points:
                while len(lower) >= 2 and xvector(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)

            for p in reversed(points):
                while len(upper) >= 2 and xvector(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)

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
        for p in self._hull_points:
            result.append([p.x, p.y])

        return result

    def demonstration(self):
        '''Plot points and convex hull for demonstration.'''
        import matplotlib.pyplot as plt

        # Console result
        hp = self.get_hull_points()
        print('Hull of ' + str(len(self._points)) +
            ' random points produces convex hull polygon of ' +
            str(len(hp) - 1) + ' points: ' + str(hp))

        # Plot result
        plt.figure('Convex Hull Demo')
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.scatter(x, y, marker='o')

        chx = [p.x for p in self._hull_points]
        chy = [p.y for p in self._hull_points]
        plt.plot(chx, chy, marker='D', color='red', linestyle='dashed')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.suptitle('Convex Hull Demonstration')
        plt.title(str(len(x)) + ' Random Points')

        plt.show()

###############################################################################

def demo():
    '''Convex Hull demonstration with plotted outputs.'''
    import random

    ch = ConvexHull(collinear=True,polygon=True)
    lo = -100
    hi = 100
    for _ in range(random.randint(40, 60)):
        ch.add1(random.randint(lo, hi), random.randint(lo, hi))

    ch.demonstration()

###############################################################################

def main2():
    '''Function to call when using input of Kattis convexhull2.'''
    ch = ConvexHull(collinear=True)
    for _ in range(int(input())):
        x, y, c = [a for a in input().split()]
        if c == 'Y':
            ch.add1(int(x), int(y))
    result = ch.get_hull_points()
    print(str(len(result)))
    for r in result:
        print(str(r.x), str(r.y))

###############################################################################

def main():
    '''Convex Hull computation of points received as formatted input'''
    while 1:
        points = int(input())
        if points == 0:
            break

        ch = ConvexHull()
        for _ in range(points):
            x, y = [int(a) for a in input().split()]
            ch.add1(x, y)

        results = ch.get_hull_points()
        print(str(len(results)))
        for p in results:
            print(str(p.x), str(p.y))

###############################################################################

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", help="convex hull demonstration", action="store_true")
    args = parser.parse_args()
    if args.demo:
        demo()
    else:
        main()
