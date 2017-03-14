bracket_pairs = {'(': ')', '{': '}', '[': ']'}


def checkio(expression: str) -> bool:
    """
    Check expression on correct bracket pairs
    :param expression: Expression in string
    :return: True or False
    """
    pool = []
    for char in expression:
        if char in bracket_pairs.keys():
            pool.append(bracket_pairs[char])
        elif char in bracket_pairs.values():
            try:
                expected = pool.pop()
            except IndexError:
                return False

            if expected != char:
                return False
    return not pool


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
