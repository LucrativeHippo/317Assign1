from math import sqrt
from math import pow
from random import randrange
from random import random
from Heuristic import get_hcost

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

    def add_edge(self, vertex1, vertex2, weight=1, undirected=True
                 , rand_num=1, rand_float=False, auto_weight=False, boardwalk=False):
        """
        Adds edge between two vertices
        :param vertex1: Start vertex
        :type vertex1: Vertex
        :param vertex2: Destination vertex
        :type vertex2: Vertex
        :param weight: Value of edge
        :param undirected: True: adds edge from vertex2 to vertex1
        :type undirected: bool

        Extra Functions
        :param rand_num: Add random int to weight from 0 to this value(exclusive)
        (default=1)
        :type rand_num: int
        :param rand_float: Use float instead of integer for rand_num
        :type rand_float: bool
        :param auto_weight: Save weight by calculating linear distance
        (default: false)
        :type auto_weight: bool
        :param boardwalk: Use boardwalk distance instead of linear distance for auto weight
        (default:false)
        :type boardwalk: bool
        :return: None
        """
        assert vertex1 is not None
        assert vertex2 is not None

        # **********EXTRA CODE STARTS HERE**********
        if auto_weight | boardwalk:  # auto weight
            if boardwalk:  # use boardwalk heuristic
                weight = abs(vertex2.x-vertex1.x)+abs(vertex2.y-vertex1)
            else:
                # auto weight linear
                weight = sqrt(
                    pow((vertex2.x-vertex1.x), 2)
                    + pow((vertex2.y-vertex1.y), 2)
                )
        # add random distance to edge
        if (rand_num > 1) | rand_float:
            if rand_float:
                weight += random * abs(rand_num)
            else:
                weight += randrange(0, rand_num)

        assert weight >= get_hcost(vertex1, vertex2)  # Weight can't be less than hcost
        # **********EXTRA CODE ENDS HERE**********

        vertex1.add_edge(vertex2, weight)
        if undirected:
            vertex2.add_edge(vertex1, weight)
