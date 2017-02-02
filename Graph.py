class Edge:
    def __init__(self, vertex, weight=0):
        self.nextVertex = vertex
        self.weight = weight


class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.edges = list()

    def add_edge(self, vertex, weight=0, undirected=True):
        self.edges.append(Edge(vertex, weight))
        if undirected:
            vertex.edges.append(Edge(self, weight))

    def __repr__(self):
        return "Vertex Fill"

class Graph:
    def __init__(self):
        self.vertex = [Vertex]

    def add_vertex(self, data=None):
        """

        :type data: object
        :param data:
        :return:
        """
        self.vertexes.append(Vertex(data))

    def addEdge(self, vertex1, vertex2, weight=0, undirected=True):
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
        if(index>=0) & (index<self.vertexes.__len__()):
            return self.vertexes[index]
        return None

    def getVertexByData(self, data):
        for v in self.vertex:
            if v.data == data:
                return v
        return None
