class Friends:
    """
    Class with social links
    """

    def __init__(self, connections):
        """
        Friends constructor
        :param connections: list or tuple of sets
        """
        self.conn = list(connections)

    def add(self, connection):
        """
        Add set in connections if not exist
        :param connection: set
        :return: True or False
        """
        if connection in self.conn:
            return False

        self.conn.append(connection)
        return True

    def remove(self, connection):
        """
        Remove set from connections if exist
        :param connection: set
        :return: True or False
        """
        if connection not in self.conn:
            return False

        self.conn.remove(connection)
        return True

    def names(self):
        """
        Get all friends names
        :return: set of unique names
        """
        return set.union(*self.conn)

    def connected(self, name):
        """
        Get set of connected friends
        :param name: Friend name
        :return: Set of names
        """
        result = set()
        for x, y in self.conn:
            if x == name:
                result.add(y)
            elif y == name:
                result.add(x)

        return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"