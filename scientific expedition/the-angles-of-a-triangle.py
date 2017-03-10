from math import acos, degrees


def angle(a, b, c):
    """
    Find the angle of the triangle by the cosine theorem
    :param a: The opposite side of the triangle
    :param b: The adjacent side of the triangle
    :param c: The adjacent side of the triangle
    :return: Angle in degrees
    """
    cos = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    if cos == 1:
        raise ValueError
    return round(degrees(acos(cos)))


def checkio(a, b, c):
    try:
        return sorted([angle(a, b, c), angle(b, a, c), angle(c, a, b)])
    except ValueError:
        return [0, 0, 0]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(2, 3, 5) == [0, 0, 0], "It's can not be a triangle"
