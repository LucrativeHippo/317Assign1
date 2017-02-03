from Graph import Vertex
from Graph import Edge
from Position import Pos
import math


def hcost(start, dest):
    """

    :type start: Pos
    :type dest: Pos
    :param start:
    :param dest:
    :return:
    """
    return math.sqrt(math.pow((start.x-dest.x), 2) + math.pow((start.y-dest.y), 2))


class AStarNode:
    def __init__(self, vertex, prev=None, gcost=0):
        """

        :type vertex: Vertex
        :type prev: AStarNode
        :param vertex: Current vertex data
        :param prev: previous AStarNode
        """
        self.node = vertex
        self.prev = prev
        if prev is not None:
            self.gCost= prev.gCost + gcost
        else:
            self.gCost=gcost


def AStar(start, dest):
    """

    :param start:
    :param dest:
    :return:
    """
    path = start

