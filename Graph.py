class Edge:
    def __init__(self, nextVertex, weight):
        """

        :param nextVertex:
        :type nextVertex: Vertex
        :param weight:
        :type weight:
        """
        self.nextVertex = nextVertex
        self.weight = weight


class Vertex:
    def __init__(self, data=None, edges=[]):
        """

        :param data:
        :type data: object
        :param edges:
        :type edges: list[Edge]
        """
        self.data = data
        self.x = data.x
        self.y = data.y
        self.edges = edges

    def add_edge(self, vertex, weight):
        # auto weight
        weight = abs(vertex.x-self.x)+abs(vertex.y-self.y)
        self.edges.append(Edge(vertex, weight))

    def __repr__(self):
        return "V(" + str(self.x) + "," + str(self.y) + ")"

    def __cmp__(self, other):
        if type(other) == type(self):
            return self.data.__cmp__(other.data)
        else:
            return self.data.__cmp__(other)

    def __hash__(self):
        return self.data.__hash__()


class Graph:
    def __init__(self):
        self.vertices = {}

    def __setitem__(self, key, value):
        """

        :param key:
        :type key:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        self.vertices[hash(key)] = value

    def __getitem__(self, item):
        """
        Gets vertex from vertices with hash item
        :param item: can be an object or a hash
        :return: Vertex with same hash as item
        :rtype: Vertex
        """
        return self.vertices.get(hash(item))

    def add_vertex(self, data=None):
        """

        :type data: object
        :param data:
        :return:
        """
        if self.__getitem__(data) is None:
            self.__setitem__(hash(data), Vertex(data=data, edges=[]))
        else:
            print("Object already exists!")

    def add_edge(self, vertex1, vertex2, weight=1, undirected=True):
        """
        Adds edge between two vertices
        :type vertex1: Vertex
        :type vertex2: Vertex
        :type undirected: bool
        :param vertex1: Start vertex
        :param vertex2: Destination vertex
        :param weight: Value of edge
        :param undirected: True: adds edge from vertex2 to vertex1
        :return: None
        """
        assert vertex1 is not None
        assert vertex2 is not None

        vertex1.add_edge(vertex2, weight)
        if undirected:
            vertex2.add_edge(vertex1, weight)
