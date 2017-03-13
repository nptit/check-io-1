import math


def spheroid_volume(a, b):
    return round(a * b ** 2 * math.pi * 4 / 3, 2)


def spheroid_area(a, b):
    if a > b:
        coof = math.acos(b / a)
        result = 2 * math.pi * (b ** 2 + b * a * coof / math.sin(coof))
    elif a < b:
        coof = math.acos(a / b)
        result = 2 * math.pi * (b ** 2 + a ** 2 / math.sin(coof) * math.log((1 + math.sin(coof)) / math.cos(coof)))
    else:
        result = 4 * math.pi * a ** 2

    return round(result, 2)


def checkio(height, width):
    return [spheroid_volume(height / 2, width / 2), spheroid_area(height / 2, width / 2)]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
