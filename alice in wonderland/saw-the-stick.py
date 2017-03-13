def get_triangle_numbers(n=1):
    """
    Infinity loop of triangle numbers
    :param n: start number
    :return:
    """
    while True:
        yield n * (n + 1) // 2
        n += 1


def checkio(number):
    """
    Break integer on max number of triangle numbers
    :param number: Max integer
    :return: list of triangle numbers
    """
    result = []
    for n in get_triangle_numbers():
        if n >= number:
            break

        result.append(n)

        while sum(result) > number:
            result.pop(0)

        if sum(result) == number:
            return result

    return []


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"