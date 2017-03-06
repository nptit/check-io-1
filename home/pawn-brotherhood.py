def calc_protector_pawns(pawn: str):
    """
    Calculate pawns can be protectors
    :param pawn:
    :return:
    """
    pawns = [
        chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1),
        chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)
    ]
    return pawns


def is_safe(pawn: str, pawns):
    """
    Check pawn is safe or not
    :param pawn:
    :param pawns:
    :return: return 1 on True or 0 on False
    """
    for protector in calc_protector_pawns(pawn):
        if protector in pawns:
            return 1

    return 0


def safe_pawns(pawns):
    """
    Count number of safe pawns
    :param pawns:
    :return:
    """
    safe = 0

    for pawn in pawns:
        safe += is_safe(pawn, pawns)

    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1