import numpy as np
# stackoverflow on Nov 9 '19 at 17:55 by clued__init__


def lineseg_dists(p, a, b):
    """Cartesian distance from point to line segment

    Edited to support arguments as series, from:
    https://stackoverflow.com/a/54442561/11208892

    Args:
        - p: np.array of single point, shape (2,) or 2D array, shape (x, 2)
        - a: np.array of shape (x, 2)
        - b: np.array of shape (x, 2)
    """
    # normalized tangent vectors
    d_ba = b - a
    d = np.divide(d_ba, (np.hypot(d_ba[:, 0], d_ba[:, 1])
                           .reshape(-1, 1)))

    # signed parallel distance components
    # rowwise dot products of 2D vectors
    s = np.multiply(a - p, d).sum(axis=1)
    t = np.multiply(p - b, d).sum(axis=1)

    # clamped parallel distance
    h = np.maximum.reduce([s, t, np.zeros(len(s))])

    # perpendicular distance component
    # rowwise cross products of 2D vectors
    d_pa = p - a
    c = d_pa[:, 0] * d[:, 1] - d_pa[:, 1] * d[:, 0]

    return np.hypot(h, c)

# sample usage
#p = np.array([0, 0])
# a = np.array([[1,  1],
#              [-1,  0],
#              [-1, -1]])
# b = np.array([[2,  2],
#              [1,  0],
#              [1, -1]])

#print(lineseg_dists(p, a, b))


# [[-0.8, -0.5]]

# [[ 0.06        0.03      ]
#  [-0.32928233  0.27506992]
#  [-0.32435697  0.04512266]]

# [[-0.32928233  0.27506992]
#  [-0.32435697  0.04512266]
#  [-0.02099459 -0.05671676]]


if __name__ == '__main__':
    lineseg_dists()  # Put the a call to the main function in the file.

# A Python3 program to find if 2 given line segments intersect or not


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Given three collinear points p, q, r, the function checks if
# point q lies on line segment 'pr'


def onSegment(p, q, r):
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
            (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise

    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/amp/
    # for details of below formula.

    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):

        # Clockwise orientation
        return 1
    elif (val < 0):

        # Counterclockwise orientation
        return 2
    else:

        # Collinear orientation
        return 0

# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.


def doIntersect(p1, q1, p2, q2):

    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True

    # Special Cases

    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True

    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True

    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True

    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    # If none of the cases
    return False

# p1 = Point(1, 1)
# q1 = Point(10, 1)
# p2 = Point(1, 2)
# q2 = Point(10, 2)
 
# if doIntersect(p1, q1, p2, q2):
#     print("Yes")
# else:
#     print("No")
 
# p1 = Point(10, 0)
# q1 = Point(0, 10)
# p2 = Point(0, 0)
# q2 = Point(10,10)
 
# if doIntersect(p1, q1, p2, q2):
#     print("Yes")
# else:
#     print("No")
 
# p1 = Point(-5,-5)
# q1 = Point(0, 0)
# p2 = Point(1, 1)
# q2 = Point(10, 10)
 
# if doIntersect(p1, q1, p2, q2):
#     print("Yes")
# else:
#     print("No")
     
# This code is contributed by Ansh Riyal