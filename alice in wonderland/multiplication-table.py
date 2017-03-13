def checkio(first, second):
    result = 0
    pin_len = len('{0:b}'.format(second))
    for pin in '{0:b}'.format(first):
        result += int(pin * pin_len, 2) ^ second
        result += int(pin * pin_len, 2) | second
        result += int(pin * pin_len, 2) & second

    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
