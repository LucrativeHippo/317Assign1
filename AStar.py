from Graph import Vertex
from Graph import Edge
from Position import Pos
import math


def get_hcost(start, dest):
    """

    :type start: Pos
    :type dest: Pos
    :param start:
    :param dest:
    :return: heuristic cost from start to dest
    """
    return math.sqrt(math.pow((start.x-dest.x), 2) + math.pow((start.y-dest.y), 2))


class AStarNode:
    def __init__(self, vertex, prev=None, gcost=0, hcost=0):
        """

        :type vertex: Vertex
        :type prev: AStarNode
        :param vertex: Current vertex data
        :param prev: previous AStarNode
        """
        self.data = vertex
        self.prev = prev
        self.hcost= hcost
        if prev is None:
            self.gCost = gcost
        else:
            self.gCost = prev.gCost + gcost


def AStar(start, dest):
    """

    :type start: Vertex
    :type dest: Vertex
    :param start: start vertex
    :param dest: destination vertex
    :return: AStarNode with path to dest from start reversed
    """
    node_list = None
    cur_node = AStarNode(start)


    while cur_node.data is not dest:

        assert isinstance(cur_node.data, Pos)
        cur_node.data.x


    return cur_node




