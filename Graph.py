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


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data=None):
        """

        :type data: object
        :param data:
        :return:
        """
        self.vertices.append(Vertex(data=data, edges=[]))

    def addEdge(self, vertex1, vertex2, weight=1, undirected=True):
        """

        :type vertex1: Vertex
        :type vertex2: Vertex
        :type undirected: bool
        :param vertex1:
        :param vertex2:
        :param weight:
        :param undirected:
        :return:
        """
        vertex1.add_edge(vertex2, weight)
        if undirected:
            vertex2.add_edge(vertex1, weight)

    def getVertexByData(self, data):
        for v in self.vertices:
            if v.data.__cmp__(data):
                return v
        return None
