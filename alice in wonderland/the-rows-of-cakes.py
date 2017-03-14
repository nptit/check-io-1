from collections import namedtuple
from math import inf

Line = namedtuple('Line', ['a', 'c', 'points'])
Point = namedtuple('Point', ['x', 'y'])
lines = []


def create_line(point_a: Point, point_b: Point) -> Line:
    """Create line from 2 points"""
    try:
        a = (point_a.y - point_b.y) / (point_a.x - point_b.x)
    except ZeroDivisionError:
        a = inf

    try:
        c = (point_a.x * point_b.y - point_b.x * point_a.y) / (point_a.x - point_b.x)
    except ZeroDivisionError:
        c = point_a.x

    return Line(a=a, c=c, points={point_a, point_b})


def get_line(a, c):
    """Get line by a coefficient and c align"""
    line = list(filter(lambda x: x.a == a and x.c == c, lines))
    if len(line) == 1:
        return line[0]

    return -1


def checkio(cakes: list) -> int:
    """
    Count number of rows of cakes
    :param cakes: List of cakes with x, y coordinates
    :return: Number of rows
    """
    global lines
    cakes = cakes[:]
    lines = []

    while cakes:
        point_a = Point(*cakes.pop())
        for point_b in cakes:
            new_line = create_line(point_a, Point(*point_b))
            exist_line = get_line(new_line.a, new_line.c)
            if -1 == exist_line:
                lines.append(new_line)
            else:
                for point in new_line.points:
                    exist_line.points.add(point)

    return sum([1 for line in lines if len(line.points) >= 3])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
