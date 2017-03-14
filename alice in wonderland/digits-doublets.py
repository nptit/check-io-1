from heapq import heapify, heappush, heappop
from collections import namedtuple

State = namedtuple('State', ['length', 'position', 'path'])


class Graph:
    """Graph for searching shortest path for doublets numbers"""

    def __init__(self):
        self._nodes = set()
        self._edges = dict()
        self._visited = set()

    def add_node(self, node):
        """Add node"""
        if node in self._nodes:
            return False

        self._nodes.add(node)
        self._edges[node] = set()
        return True

    def add_edge(self, start, end):
        """Add edge"""
        self.add_node(start)
        self.add_node(end)
        self._edges[start].add(end)
        self._edges[end].add(start)

        return True

    def find_path(self, start, end):
        """Find shortest path from start to end node. A-star algorithm"""
        if start not in self._nodes and end not in self._nodes:
            raise ValueError

        queue = [State(len([start]), start, [start])]
        heapify(queue)

        while queue:
            current = heappop(queue)

            if current.position == end:
                return current.path

            if current.position in self._visited:
                continue

            for next_position in self._edges[current.position]:
                if next_position in self._visited:
                    continue
                heappush(queue, State(current.length + 1, next_position, current.path[:] + [next_position]))

            self._visited.add(current.position)

        return []


def compare_digits(a: int, b: int) -> int:
    """
    Compare 2 number by different digits
    :param a: First number
    :param b: Second number
    :return: Number of different digits
    """
    a, b = map(str, [a, b])
    length = diff = max(len(a), len(b))
    a, b = map(lambda x, l=length: x.zfill(l), [a, b])
    for i in range(length):
        diff -= 1 if a[i] == b[i] else 0

    return diff


def checkio(numbers):
    graph = Graph()

    copy = numbers[:]
    while copy:
        node = copy.pop()
        for number in copy:
            if compare_digits(node, number) == 1:
                graph.add_edge(node, number)

    return graph.find_path(numbers[0], numbers[-1])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
