def checkio(data):
    return data[0] if len(data) == 1 else data.pop() + checkio(data)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3]) == 6, "1 + 2 + 3 == 6"
