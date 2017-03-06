def checkio(data: int):
    """
    Converts a number from decimal to Roman numerals
    :param data: decimal integer 0 < data < 4000
    :return: Roman numeral
    """
    converter = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    output = ''

    for key in sorted(converter.keys(), reverse=True):
        while data >= key:
            output += converter[key]
            data -= key

    return output


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'