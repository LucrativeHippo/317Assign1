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
    def __init__(self, data=None, edges=list()):
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

    def add_edge(self, vertex, weight, undirected=True):
        self.edges.append(Edge(vertex, weight))
        if undirected:
            vertex.edges.append(Edge(self, weight))

    def __repr__(self):
        return "Vertex: " + str(self.x) + " " + str(self.y)


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, data=None):
        """

        :type data: object
        :param data:
        :return:
        """
        self.vertices.append(Vertex(data=data))

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
        vertex1.add_edge(vertex2, weight, undirected)

    def getVertexByIndex(self, index):
        if(index>=0) & (index<self.vertices.__len__()):
            return self.vertices[index]
        return None

    def getVertexByData(self, data):
        for v in self.vertices:
            if v.data.__cmp__(data):
                return v
        return None
