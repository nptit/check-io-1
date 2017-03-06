def checkio(data: list):
    """
    Removes the given list all non-unique values
    :param data: list of elements
    :return: list with non-unique elements only
    """
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    result = []
    for item in data:
        if data.count(item) > 1:
            result.append(item)
    return result


# Some tests
if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
