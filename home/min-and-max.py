def min(*args, **kwargs):
    minimum = None
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    for x in args:
        if minimum is None or key(x) < key(minimum):
            minimum = x

    return minimum


def max(*args, **kwargs):
    maximum = None
    key = kwargs.get("key", lambda x: x)
    if len(args) == 1:
        args = args[0]
    for x in args:
        if maximum is None or key(x) > key(maximum):
            maximum = x

    return maximum


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"