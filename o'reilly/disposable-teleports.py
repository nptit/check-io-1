class Platform:
    def __init__(self, edges: str=None):
        """
        Constructor
        :param edges: String of edges
        """
        self._nodes = set()
        self._graph = dict()
        self._visited = []
        self._path = []

        if edges is not None:
            for x, y in edges.split(','):
                self.add_node(x)
                self.add_node(y)
                self.add_edge(x, y)

    def add_node(self, node):
        """
        Add node to set
        :param node:
        :return: True or False
        """
        if node in self._nodes:
            return False

        self._nodes.add(node)
        self._graph[node] = set()
        return True

    def add_edge(self, x, y):
        """
        Add edge to dictionary
        :param x: First point of edge
        :param y: Second point of edge
        :return: True or False
        """
        if x not in self._nodes and y not in self._nodes:
            return False

        self._graph[x].add(y)
        self._graph[y].add(x)
        return True

    def find_path(self):
        """
        Find hamilton path from 1 to 1 node
        :return: String with path
        """
        if self._hamilton("1"):
            return ''.join(self._path)
        return None

    def _hamilton(self, current_node):
        """
        Hamilton loop algorithm
        :param current_node: Current node
        :return: True or False
        """
        self._path.append(current_node)
        if len(set(self._path)) == len(self._nodes):
            if self._path[-1] in self._graph[self._path[0]] and {self._path[0], self._path[-1]} not in self._visited:
                self._path.append(self._path[0])
                return True
            else:
                self._path.pop()
                return False

        for next_node in self._graph[current_node]:
            if {current_node, next_node} not in self._visited:
                self._visited.append({current_node, next_node})
                if self._hamilton(next_node):
                    return True
                self._visited.remove({current_node, next_node})
        self._path.pop()

        return False


def checkio(teleports_string: str):
    """
    Find path in labyrinth of portal laid from all portals
    :param teleports_string: string with portal relations delimited with ','
    :return:
    """
    platform = Platform(teleports_string)
    graph = platform.find_path()

    return graph


# This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"