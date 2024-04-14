class Edge:
    def __init__(self, vertex_from: int, vertex_to: int, weight: int):
        self.vertex_to = vertex_to
        self.vertex_from = vertex_from
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:
    def __init__(self, size: int):
        self.__size = size
        self.__adjacency_list = [[] for _ in range(size)]

    def add_edge(self, vertex_from: int, vertex_to: int, weight: int):
        self.__adjacency_list[vertex_from].append(Edge(vertex_from, vertex_to, weight))
        self.__adjacency_list[vertex_to].append(Edge(vertex_to, vertex_from, weight))

    def get_neighbours(self, vertex: int):
        return self.__adjacency_list[vertex]
